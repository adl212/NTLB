// var table = document.getElementById("table");
// var json = json.parse("/data.json");
// var num;

// for (num = 0; json.length; num++) {
//   var userProfile = userLink(num);

//   table.innerHTML = "<tr><td>" + json.users[num].carID + "</td><td><a href='" + userProfile + "'" + json.users[num].displayname + "</td><td>" + json.users[num].races + "</td><td>" + json.users[num].speed + "</td><td>" + json.users[num].accuracy + "</td><td>" + json.users[num].points"</td></tr>";
// }


// function userLink(user) {
//   var username = json.users[user].username;
//   var link = "https://www.nitrotype.com/racer/" + username;

//   return link;
// }

var xmlhttp = new XMLHttpRequest();
xmlhttp.onreadystatechange = function() {
  if (this.readyState == 4 && this.status == 200) {
    var json = JSON.parse(this.responseText);
    console.log(json);
  }
};
xmlhttp.open("GET", "data.json", true);
xmlhttp.send();

// var json = JSON.parse("/data.json");
// var consoleLog = json.users[0].carID;

// console.log(consoleLog);