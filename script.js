const options = {
    // Required: API key
    key: '3wxwm4eBQW1ExUnI36k36OabrGCpPvKX', // REPLACE WITH YOUR KEY !!!

    // Put additional console output
    verbose: true,

    // Optional: Initial state of the map
    lat: 39.6136888,
    lon: 2.6307834,
    zoom: 6,
};

// Initialize Windy API
windyInit(options, windyAPI => {
    // windyAPI is ready, and contain 'map', 'store',
    // 'picker' and other usefull stuff

    const  {map}  = windyAPI;
    // .map is instance of Leaflet map

    L.popup()
        .setLatLng([39.6, 2.63])
        .setContent('Hello World')
        .openOn(map);

});

function getCoordinatesClient(event){
    var cX = event.clientX;
    var cY = event.clientY;
    var coords1 = "Screen: X: " + cX + ", Y coords: " + cY;
    document.getElementById("demo").innerHTML = coords1;

    var coordinate = L.map.panBy(L.point(200, 300));
    document.getElementById("demo2").innerHTML = coordinate;
}
