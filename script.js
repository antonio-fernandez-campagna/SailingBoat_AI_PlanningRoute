//3wxwm4eBQW1ExUnI36k36OabrGCpPvKX
var mymap = L.map('mapid').setView([39.1, 1.77], 8);
L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}', {
    attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
    maxZoom: 18,
    id: 'mapbox/streets-v11',
    tileSize: 512,
    zoomOffset: -1,
    accessToken: 'pk.eyJ1Ijoibmlub2ZkeiIsImEiOiJja2VvaWUxa2QyN3YxMnNwY3BkNHY1eGdvIn0.W4tN1eMuhJ_lFd4lGtUhZA'
}).addTo(mymap);

var coord = new mymap.MercatorCoordinate(39.6735, 2.357); // 6914.281956295339
alert(coord.toAltitude())

function getCoordinatesByForm() {

  var latitudeStart = document.getElementById("latitudeStart").value;
  var longitudeStart = document.getElementById("longitudeStart").value;
  var latitudeDestination = document.getElementById("latitudeDestination").value;
  var longitudeDestination = document.getElementById("longitudeDestination").value;


  var start = [latitudeStart, longitudeStart];
  var destination = [latitudeDestination, longitudeDestination];


  var polyline = L.polyline(var_test_lan, {color: 'red'}).addTo(mymap);
  // zoom the map to the polyline

  map.fitBounds(polyline.getBounds());

}



function create_map(start, destination){

}
