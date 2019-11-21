function showmessage(){
	alert("HELLO")
}
function mouseover(){
	alert("MOUSE OVER")
}

function getlocation(){
	var loc_name=document.getElementById("id_name")
	var loc_lat=document.getElementById("id_latitude")
	var loc_long=document.getElementById("id_longitude")
	navigator.geolocation.getCurrentPosition(fill_loc)
	function fill_loc(position){
		lat =  position.coords.latitude
		long = position.coords.longitude
		loc_name.value="adres1"
		loc_lat.value=lat
		loc_long.value=long

	}
	
}