////////////////////////////////////////////////////
// alpha.js
///////////////////////////////////////////////////

var alphabet = "abcdefghijklmnopqrstuvwxyz";

names = ["amy kat", "berry jam", "dan ricky", "joe leaf", "joel kardi", "rik kart", "steve pete", "steve pratt", "zarg hat"];
jsonNames = jsonify(names);

alpha1 = indexIsGoesAfter(jsonNames);

document.getElementById("names").innerHTML = alpha1;

function jsonify(list) {
    
    jsonList = [];
    
    for (var i = 0; i < list.length; i++) {
        var spaceIndex = list[i].indexOf(" ");
        var first = list[i].slice(0, spaceIndex);
        var last = list[i].slice(spaceIndex, list[i].length);
        jsonList.push({ "first" :  first  , "last" : last });
    }
  
    return jsonList;
}


function goesBefore(newJsonName, oldJsonName) {
  
  //returns true if new goes before old, false otherwise
  
  var newLast = newJsonName.last;
  var newFirst = newJsonName.first;
  var oldLast = oldJsonName.last;
  var oldFirst = oldJsonName.first;
  
  for (var i = 0; i < Math.min(newLast.length, oldLast.lenght); i++) {
    
    if (newLast == oldLast) {
      break;
    }
    
    if (alphabet.indexOf(newLast[i]) > alphabet.indexOf(oldLast[i])) {
      return false;
    } else if (alphabet.indexOf(newLast[i]) < alphabet.indexOf(oldLast[i])) {
      return true;
    }
   
  }
  
  //same last names
  for (var i = 0; i < Math.min(newFirst.length, oldFirst.lenght); i++) {
    
    if (newFirst == oldFirst) {
      //same name, doesnt matter
      return false;
    }
    
    if (alphabet.indexOf(newLast[i]) > alphabet.indexOf(oldLast[i])) {
      return false;
    } else if (alphabet.indexOf(newLast[i]) < alphabet.indexOf(oldLast[i])) {
      return true;
    }
    
  }
  
}


//alg 1
function indexIsGoesAfter(jsonList) {
  
  //put each name at the index that is same num as how many names it is after
  
  var alphaJsonList = jsonList;
  
  for (var i = 0; i < jsonList.length; i++) {
    var numGoesAfter = 0;
    for (var j = 0; j < jsonList.length && j != i; i++) {
      if (!goesBefore(jsonList[i], jsonList[j])) {
        numGoesAfter += 1;
      }      
    }
    alphaJsonList[numGoesAfter] = jsonList[i];
  }
  
  return alphaJsonList;  
}



















// function numberize(letter) {
//   for (var i = 0; i < alpha.length; i++) 
//     if (alpha[i].toLowerCase() === letter.toLowerCase()) {
//       return i;
//     } 
// }

// function put_in_alpha(list, new_word) {
//   var alpha_list = [];
  
//   if (list === []) {
//     alpha_list.push(new_word);
//     return alpha_list;
//   }
  
//   for (var i = 0; i < list.length; i++) {

//     for (var j = 0; j < list[i].length; j++) {
    
//       if (list[i][j] == " " && new_word[j] == " ") { //same first name
//         alert("hi");
//         continue;
//       } else if (list[i][j] == " " && new_word[j] != " ") { //same but new longer
//         alpha_list.push(new_word);
//         for (var k = i; k < list.length; k++) {
//           alpha_list.push(list[k]);
//         }
//         return alpha_list;
//       } else if (list[i][j] != " " && new_word[j] == " ") { //same but old longer
//         alert("hi");
//         alpha_list.push(new_word);
//         for (var k = i; k < list.length; k++) {
//           alpha_list.push(list[k]);
//         }
//         return alpha_list;
//       }

//       if (alphabet.indexOf(new_word[j]) < alphabet.indexOf(list[i][j])) {
//         alpha_list.push(new_word);
//         for (var k = i; k < list.length; k++) {
//           alpha_list.push(list[k]);
//         }
//         return alpha_list;
//       } else if (j + 1 > list[i].length) {
//         alpha_list.push(list[i]);
//       } else {
//         alpha_list.push(list[i]);
//         break;
//       }
//     }
//   }  
// }
  
// function alphabetize(list) {
//   var final_alpha = [];
//   for (var i = 0; i < list.length; i++) {
//     final_alpha = put_in_alpha(final_alpha, list[i]);
//   }
//   return final_alpha;
// }
