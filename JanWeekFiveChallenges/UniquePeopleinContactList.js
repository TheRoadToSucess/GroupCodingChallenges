// You are given a two-dimensional list of strings contacts. Each element contacts[i] represents the list of emails for contact i. 
// Contact i is considered a duplicate if there's a j < i such that contact j shares a common email with i. Return the number of 
// unique people in contacts.



contacts = [
    ["elon@tesla.com", "elon@paypal.com"],
    ["elon@tesla.com", "elon@spacex.com"],
    ["tim@apple.com"]
]

let names = [];
let counter = 0;
if(contacts.length == 1){
    console.log(1);
}else{
contacts.forEach(contact =>{
    contact.forEach(email =>{
        names[counter] = email.substring(0,email.indexOf('@'));
        counter++;
    })
});
var uniqueNames = names.filter(onlyUnique);

console.log(uniqueNames.length);

function onlyUnique(value, index, self) {
  console.log(self.indexOf(value) === index);
}

}

