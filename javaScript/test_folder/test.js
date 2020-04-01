var lat1 = 45.5289;
var lon1 = -122.4582;
var lat2 = 45.615849;
var lon2 = -122.4932303;

var y = Math.sin(lon2-lon1) * Math.cos(lat2);
var x = Math.cos(lat1)*Math.sin(lat2) - Math.sin(lat1)*Math.cos(lat2)*Math.cos(lon2-lon1);
var brng = Math.atan2(y, x);
var deg = brng * (180 / Math.PI)
console.log(deg, "this is brng")

heading = (231 + brng) % 360;

console.log(heading, "this is heading")
// the above text is a test that i was running.

