let words = ["java", "beans"];
// words.join('');
// console.log(words.join());

// console.log(words.split(","));


// words.forEach((item, index) =>{
// // index[1] 
// // item == 'beans' ? item.replace('beans','Beans')

// if(item == 'beans'){
//     console.log(item.replace("beans","Beans"));
//     console.log(words.join());

//     console.log(item)
// }


// // console.log(index, item);


// })

let results = words[0].toLowerCase()

for (let i = 1; i < words.length; i++) {
    results += words[i][0].toUpperCase() + words[i].substring(1).toLowerCase()
}

console.log(results)

// try printing method call

