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


    var xhr = new XMLHttpRequest();

    $( document ).ready(function() {
        let endpoint = 'http://api.opencagedata.com/geocode/v1/json?q='+latitude+'+'+longitude+'&key=add439a2f90b4b15836d85155ffb848e';


        var request = new XMLHttpRequest();

        request.open('GET', endpoint, true);

        request.onload = function ()
        {
            if (this.status >= 200 && this.status < 500)
            {
                // Success!
                var data = JSON.parse(this.response);
                console.log(data.results[0].formatted);
                document.getElementById("id_location").value = data.results[0].formatted;


            } else
            {
                // We reached our target server, but it returned an error.
                console.log("Error status not between 200 and 400.");
            }
        };

        request.onerror = function (e)
        {
            // There was a connection error of some sort.
            console.log(e);
        };
        request.send();


      });

}
function onErrorGeo(err){
    console.log(err);
}


$("#id_longitude").change(function(e){
    console.log("CHIKAA WIGGAA");

    onSuccessGeoredef(document.getElementById("id_longitude").value,document.getElementById("id_latitude").value);

});
$("#id_latitude").change(function(e){
    console.log("NIGGAAA WIGGAA");
    onSuccessGeoredef(document.getElementById("id_longitude").value,document.getElementById("id_latitude").value);

    });

    function onSuccessGeoredef(longitude,latitude){

        console.log(latitude);
        console.log(longitude);
        console.log("REVERSING LIKE A PRO,FLEXING LIKE A NIGGA");
        // getReverseGeocodingData(latitude,longitude);
        document.getElementById("id_latitude").value = latitude;
        document.getElementById("id_longitude").value = longitude;


        var xhr = new XMLHttpRequest();

        $( document ).ready(function() {
            let endpoint = 'http://api.opencagedata.com/geocode/v1/json?q='+latitude+'+'+longitude+'&key=add439a2f90b4b15836d85155ffb848e';


            var request = new XMLHttpRequest();

            request.open('GET', endpoint, true);

            request.onload = function ()
            {
                if (this.status >= 200 && this.status < 500)
                {
                    // Success!
                    var data = JSON.parse(this.response);
                    console.log(data.results[0].formatted);
                    document.getElementById("id_location").value = data.results[0].formatted;


                } else
                {
                    // We reached our target server, but it returned an error.
                    console.log("Error status not between 200 and 400.");
                }
            };

            request.onerror = function (e)
            {
                // There was a connection error of some sort.
                console.log(e);
            };
            request.send();


          });

    }


    function onSuccessGeoForward(loc){

        console.log("FWDING");
        // getReverseGeocodingData(latitude,longitude);



        var xhr = new XMLHttpRequest();

        $( document ).ready(function() {
            let endpoint = 'https://api.opencagedata.com/geocode/v1/json?q='+loc+'&key=add439a2f90b4b15836d85155ffb848e';


            var request = new XMLHttpRequest();

            request.open('GET', endpoint, true);

            request.onload = function ()
            {
                if (this.status >= 200 && this.status < 500)
                {
                    // Success!
                    var data = JSON.parse(this.response);
                    console.log(data);
                    // document.getElementById("id_location").value = data.results[0].formatted;
                    document.getElementById("id_latitude").value = data.results[0].geometry.lat;
                    document.getElementById("id_longitude").value = data.results[0].geometry.lng;

                }
                else
                {
                    // We reached our target server, but it returned an error.
                    console.log("Error status not between 200 and 400.");
                }
            };

            request.onerror = function (e)
            {
                // There was a connection error of some sort.
                console.log(e);
            };
            request.send();


          });

    }

    $("#id_location").change(function(e){
        console.log("NIGGAAA WIGGAA");
        onSuccessGeoForward(document.getElementById("id_location").value);

        });