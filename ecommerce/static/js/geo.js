//   GEOAPI

if(navigator.geolocation){
    navigator.geolocation.getCurrentPosition(onSuccessGeo,onErrorGeo)
}
else{
    console.log("UNAUTH");

}

function onSuccessGeo(pos){
    const {latitude,longitude} = pos.coords;
    console.log(latitude);
    console.log(longitude);
    console.log("REVERSING LIKE A PRO,FLEXING LIKE A NIGGA");
    // getReverseGeocodingData(latitude,longitude);
    document.getElementById("id_latitude").value = latitude;
    document.getElementById("id_longitude").value = longitude;