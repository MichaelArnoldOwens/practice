'''
Given a distance d, a pendulum starts at d and swings from d to negative d and back. For example, given distance 3, the pendulum goes 3, 2, 1, 0, -1, -2, -3, -2, -1, 0, 1, 2, 3, and back again. 
Given a time t, return the pendulum's position. The time starts at 0.

3, 2, 1, 0, -1, -2, -3, -2, -1, 0, 1, 2, 3,
0  1. 2. 3.  4.  5   6.  7.  8  9. 10 11 12

In this example, 0 returns 3, 1 returns 2, 3 returns 0, and so on.

Follow-up:
What if the pendulum reduces by 1 distance per full swing? For example, for distance 3, the pendulum would go 3, 2, 1, 0, -1, -2, -3, -2, -1, 0, 1, 2, 1, 0, -1, -2, -1, 0, 1, 0, -1, 0 and then stay on 0 from this point forward.
'''
//brute force
function pendulum(distance, time) {
  let position = distance;
  let increment = -1;
  while (time > 0) {
    position += increment;

    if (position === -distance) {
      increment = 1;
    }
    if (position === distance) {
      increment = -1;
    }
    time--;
  }
  return position;
}

//O(1)
function pendulum(distance, time) {
  const lapLength = distance * 2;
  const lapsCompleted = Math.floor(time / lapLength);
  const timeIntoLap = time % lapLength;

  const position = (distance - timeIntoLap) * (lapsCompleted % 2 === 0 ? 1 : -1);
  // handle an odd javascript quirk of negative zero!
  return position === -0 ? 0 : position;
}

// OR

function pendulum(d, t) {
  const cycle = d * 4;
  t = t % (cycle || 1);

  return t > d * 2
    ? d * -3 + t
    : d - t;
}


console.log(pendulum(2, 0), 2);
console.log(pendulum(2, 1), 1);
console.log(pendulum(2, 2), 0);
console.log(pendulum(2, 3), -1);
console.log(pendulum(2, 4), -2);
console.log(pendulum(2, 5), -1);
console.log(pendulum(2, 6), 0);
console.log(pendulum(2, 8), 2);
console.log(pendulum(2, 9), 1);

console.log(pendulum(5, 0), 5);
console.log(pendulum(5, 3), 2);
console.log(pendulum(5, 8), -3);
console.log(pendulum(5, 9), -4);
console.log(pendulum(5, 10), -5);
console.log(pendulum(5, 11), -4);
console.log(pendulum(5, 19), 4);
console.log(pendulum(5, 20), 5);
console.log(pendulum(5, 21), 4);

console.log(pendulum(3, 0), 3);
console.log(pendulum(3, 1), 2);
console.log(pendulum(3, 2), 1);
console.log(pendulum(3, 3), 0);
console.log(pendulum(3, 4), -1);
console.log(pendulum(3, 5), -2);
console.log(pendulum(3, 6), -3);
console.log(pendulum(3, 7), -2);
console.log(pendulum(3, 9), 0);
console.log(pendulum(3, 12), 3);
console.log(pendulum(3, 13), 2);
