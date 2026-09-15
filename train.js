function findDoublers(str) {
  const seen = new Set();
  for (const ch of str) {
    if (seen.has(ch)) {
      return true; // Agar harf takrorlansa
    }
    seen.add(ch);
  }
  return false; // Hech bir harf takrorlanmasa
}

// Misollar:
console.log(findDoublers("hello")); // true
console.log(findDoublers("world")); // false
console.log(findDoublers("java")); // true
console.log(findDoublers("python")); // false

//f task
// function getHighestIndex(arr) {
//   let max = arr[0];
//   let index = 0;

//   for (let i = 1; i < arr.length; i++) {
//     if (arr[i] > max) {
//       max = arr[i];
//       index = i;
//     }
//   }
//   return index;
// }

// // Misol:
// console.log(getHighestIndex([5, 21, 12, 21, 8])); // 1
