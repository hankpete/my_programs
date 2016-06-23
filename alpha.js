var alphabet = "abcdefghijklmnopqrstuvwxyz";
var names = ["Henry Peterson", "Carol Rosenfield", "Jim Sullivan"];

//names = alphabetize(names);

names = ["amy kat", "berry jam", "dan ricky", "joe leaf", "joel kardi", "rik kart", "steve pete", "steve pratt", "zarg hat"];
// names = put_in_alpha(names, "cara pete");
// names = put_in_alpha(names, "joeseph tail");
// names = put_in_alpha(names, "dan ricker");
// names = put_in_alpha(names, "be me");
// names = put_in_alpha(names, "amy katherine");
jsonNames = jsonify(names);

// d3.select("body").selectAll("p")
//     .data(names)
//   .enter()
//     .append("p")
//     .text(function(d) {return d;});

function jsonify(list) {
    jsonList = [];
    for (var i = 0; i , list.length; i++) {
        var spaceIndex = list[i].indexOf(" ");
        var first = list[i].slice(0, spaceIndex);
        var last = list[i].slice(spaceIndex, list[i].length);
        jsonList.push('{ "first":' + first + ', "last":' + last + ' }');
    }
    return jsonList;
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

