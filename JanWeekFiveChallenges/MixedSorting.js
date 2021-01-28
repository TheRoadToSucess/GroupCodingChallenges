let nums = [8, 13, 11, 90, -5, 4];
let odd = [];
let even = [];
let answer = [];

const isEven = (n) => {
  // function isEven(n) {
  return n % 2 == 0;
};

const isOdd = (n) => {
  //  function isOdd(n) {
  return Math.abs(n % 2) == 1;
};

const sorter = () => {
  nums.forEach((item, index) => {
    isEven(item)
      ?  even.push(item)
      : isOdd(item)
      ? odd.push(item)
      : false;

   

  });
};

sorter();
console.log(even);

console.log(odd);
console.log(nums);


    //   if (isEven(item)){
    //     console.log(index, item);
    //   }
    //   else if (isOdd(item)){
    //     console.log(index, item)
    //   }
    //   else{
    //       false
    //   }

// return mycondition1 ? console.log(`if(?) my condition ${mycondition1} print this`)
// : nextcondition1 > 0 && otherCondition1 > 0 ? console.log(`if(?) my condition ${nextcondition1} greater than do this`)
// // : nextcondition > 0 ? doThat
// : recursionRecallMethod();

// thelistofEach.forEach((item, index) => {
//     console.log(index, item);
// }); // how to do with for of
