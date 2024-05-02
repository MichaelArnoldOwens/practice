/*
 * create a React hook called useQuery() => {loading, data, error, trigger, cancel}
 *
 * { 
 *  loading: boolean
 *  data: [{..}, ...]
 *  error: Error
 *  trigger: (query) => void
 *  cancel: () => void
 * }
 * 
 *  the hook will:
 *    1. make a post request to get a token
 *    2. make a get request repeatedly with the token at an interval of 1 minute while UNAVAILABLE. When AVAILABLE, query without any delay until DONE status is reached
 *    3. cancel should cancel the request
 *    4. catch api and http errors
 *
 * follow-ups: 
 *  a. handle multiple trigger calls
 *  b. only allow one single call to exist at a time
 *  c. allow multiple calls to exist at a time
 *
 */
import { useState, useEffect, useCallback } from "react";

const useQuery = () => {
  const [isLoading, setIsLoading] = useState(false);
  const [data, setData] = useState([]);
  const [error, setError] = useState(null);
  const [intervalId, setIntervalId] = useState(null);
  const [controller, setController] = useState(new AbortController());
  const signal = controller.signal;

  const cancel = () => {
    controller.abort();
    setController(new AbortController());
    clearInterval(intervalId);
    setIsLoading(false); // Reset isLoading on cancel
  };

  const fetchData = useCallback(async (query) => {
    try {
      if (isLoading) {
        cancel();
      }
      setIsLoading(true);

      const response = await fetch(query, { signal });

      if (!response.ok) {
        const error = `HTTP Error ${response.status}`;
        setError(error);
        throw new Error(error);
      }

      const { token } = await response.json();

      let interval = 1000;
      const intervalId = setInterval(async () => {
        const queryResponse = await fetch(`/query/${token}`, { signal });

        if (!queryResponse.ok) {
          const error = `HTTP Error ${queryResponse.status}`;
          setError(error);
          throw new Error(error);
        }

        const { type, data, error } = await queryResponse.json();

        if (error) {
          setError(error);
          clearInterval(intervalId);
          return;
        }
        if (type === "AVAILABLE") {
          interval = 0;
          setData(prevData => [...prevData, data]);
        } else if (type === "DONE") {
          setData(prevData => [...prevData, data]);
          setIsLoading(false);
          clearInterval(intervalId);
        }
      }, interval);
      setIntervalId(intervalId);
    } catch (e) {
      setError(e.message);
      setIsLoading(false);
    }
  }, [signal, isLoading, cancel]);

  useEffect(() => {
    return () => cancel();
  }, [cancel]);

  return { isLoading, data, error, fetchData, cancel };
};
