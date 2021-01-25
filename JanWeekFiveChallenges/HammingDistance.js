let x = 9
let y = 5

// function convertToBinary(x, y) {
//     let bin = 0;
//     let rem, i = 1, step = 1;
//     while (x && y != 0 ) {
//         rem = x % 2;
//         console.log(
//             `Step ${step++}: ${x}/2, Remainder = ${rem}, Quotient = ${parseInt(x/2)}`
//         );
//         x = parseInt(x / 2);
//         bin = bin + rem * i;
//         i = i * 10;
//     }
//     console.log(`Binary: ${bin}`);
// }

// // take input
// convertToBinary(x, y);

// u can also to bin(x) in python show real quick
// let i = 0;
// for(i in range((0, 32))){

// }

// let bit = Integer.bitCount(x ^ y);

// console.log(bit);


const bin = x.toString(2); 

console.log(bin);