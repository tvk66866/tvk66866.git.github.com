<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.0/jquery.min.js"> </script>

<script>
//setup some JSON to use
var cars = [
	{ "make":"Porsche", "model":"911S" },
	{ "make":"Mercedes-Benz", "model":"220SE" },
	{ "make":"Jaguar","model": "Mark VII" }
];

window.onload = function() {
	// setup the button click
	document.getElementById("theButton").onclick = function() {
		doWork()
	};
}

function doWork() {
	// ajax the JSON to the server
	$.post("output", cars, function(){

	});
	// stop link reloading the page
 event.preventDefault();
}
</script>
This will send data using AJAX to Python:<br /><br />
<a href="" id="theButton">Click Me</a>