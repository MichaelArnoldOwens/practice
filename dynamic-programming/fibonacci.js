function fibRecursive(n) {
  callCount++;
  if (n === 1 || n === 2) {
    return 1;
  }

  return fibRecursive(n - 1) + fibRecursive(n - 2);
}

let callCount = 0;
console.log(`fibRecursive(${10}) = ${fibRecursive(10)}, call count: ${callCount}`);

callCount = 0;
console.log(`fibRecursive(${12}) = ${fibRecursive(12)}, call count: ${callCount}`);

function fibMemoized(n) {
  // start out with the base cases in our memo.
  const memo = {1: 1, 2: 1}

  // This helper looks mostly like the strictly recursive version.
  function fib(n) {
    callCount++;

    // Check the memo for a previously computed answer.
    if (memo[n] !== undefined) {
      return memo[n];
    }

    // Store new answers in the memo before returning.
    memo[n] = fib(n-1) + fib(n-2);
    return memo[n];
  }
  return fib(n);
}

function fibDP(n) {
  // Just like memoization, we start with our base cases in the table.
  const table = {1: 1, 2: 1};

  // Now start small and build up without recursion!
  for (let i = 3; i <= n; i++) {
    table[i] = table[i - 1] + table[i - 2];
  }

  return table[n];
}

console.log(`fibDP(${20}) = ${fibDP(20)}`);


function basicDynamicProgrammingPattern(/* parameters */) {
 // Create table

 // Fill in initial table values from recursive base cases

 // for each cell in the table
   // compute new cells value based on previous values

  // return desired cell
}

function fibDP(n) {
  // For this problem we can create the table and fill in initial values in one step. We
  // look at the recursive base cases to decide what needs to be filled in.
  const table = {1: 1, 2: 1};

  // The table is just one dimensional, so the iteration part of the pattern
  // is just to count up to our desired solution.
  for (let i = 3; i <= n; i++) {

    // To compute a new cell, we look to the recursive steps above:
    //   return fibRecursive(n - 1) + fibRecursive(n - 2);
    //
    // This tells us that to compute a new cell, we need to look in two other cells and
    // add their values. Which cells? The cell before the one we are computing (i - 1) 
    // and the one before that (i - 2).
    table[i] = table[i - 1] + table[i - 2];
  }

  // After filling in the table, we return the result we want!
  return table[n];
}
