/*
 * create a React hook called useQuery() => {loading, data, error, trigger, cancel}
 *
 * follow-ups: 
 *  a. handle multiple trigger calls
 *  b. only allow one single call to exist at a time
 *  c. allow multiple calls to exist at a time
 *
 */
import {useState} from 'react'
const useQuery = () => {
  const [isLoading, setIsLoading] = useState(false) 
  const [data, setData] = useState([])
  const [error, setError] = useState(null)
  const [intervalId, setIntervalId] = useState(null)
  const [controller, setController] = useState(new AbortController());
  const signal = controller.signal

  const cancel = () => {
    controller.abort()
    setController(new AbortController())
    clearInterval(intervalId)
  }

  const trigger = (query) => fetch(query, {post, signal}).then(response => { // wrap in useCallback() ?
    if (isLoading) {
      cancel()
    }
    setIsLoading(true)
      if (response.status === 200) {
      return response.json
      } else {
        setError(`HTTP Error ${response.status}`)
      }
    }).then(({token}) => {
      let interval = 1000
      const intervalId = setInterval(() => {
        fetch(`/query/${token}`, { signal }).then(response => {
          if (response.status === 200) {
            response.json()
          } else {
              setError(`HTTP Error ${response.status}`)
          }
      }).then(({type, data, error })=> {
              if (error) {
                setError(error)
                clearInterval(intervalId)
                return
              }
              if (type === 'AVAILABLE') {
                interval = 0
                setData(d => [...d, data])
              } else if (type === 'DONE') {
                setData(d => [...d, data])
                setIsLoading(false)
                clearInterval(intervalId)
                return
              }
            })
      }, interval)
      setIntervalId(intervalId)
    }).catch(e => setError(e))

  

  return {isLoading, data, error, trigger, cancel}
}
