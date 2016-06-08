var alpha = "abcdefghijklmnopqrstuvwxyz";
var names = ["Henry Peterson", "Carol Rosenfield", "Jim Sullivan"];

names = alphabetize(names);

d3.select("body").selectAll("p")
    .data(names)
  .enter()
    .append("p")
    .text(function(d) {return d;});

function numberize(letter) {
  for (var i = 0; i < alpha.length; i++) 
    if (alpha[i].toLowerCase() === letter.toLowerCase()) {
      return i;
    } 
}

function put_in_alpha(list, new_word) {
  var alpha_list = [];
  
  if (list === []) {
    alpha_list.push(new_word);
    return alpha_list;
  }
  
  for (var i = 0; i < list.length; i++) {
    for (var j = 0; j < list[i].length; j++) {
      if (list[i][j] === " " || new_word[j] === " ") {
        continue;
      }
      if (numberize(list[i][j]) < numberize(new_word[j])) {
          alpha_list.push(new_word);
          for (var k = j; k < list.length; k++) {
            alpha_list.push(list[k]);
          }
          return alpha_list;
      } else if (j + 1 > list[i].length) {
        alpha_list.push(list[i]);
      } 
    }
  }  
}
  
function alphabetize(list) {
  var final_alpha = [];
  for (var i = 0; i < list.length; i++) {
    final_alpha = put_in_alpha(final_alpha, list[i]);
  }
  return final_alpha;
}
