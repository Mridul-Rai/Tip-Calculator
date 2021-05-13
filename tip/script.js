 // script.js

//Custom function
function calculatorTip() {
	 // store the data of inputs
	 var billAmount = document.getElementById("billAmount").value;
	 var serviceQuality = document.getElementById("serviceQuality").value;
	 var numpeople = document.getElementById("totalPeople").value;
	 //Quick validation
	 if(billAmount === "" || serviceQuality == 0) {
	 	window.alert("Please enter some values to get this baby up and running!");
	 	return; //this will prevent the function from continuing
	 }
	 //Check to see if this input is empty or less than or equal to 1
	 if(numPeople === "" || numPeople <= 1) {
	 	numPeople = 1;
	 	document.getElementById("each").style.display = "none";
	 } 
	else {
	 	document.getElementById("each").style.display = "block";
	 }
	 // Do some math!
	 var total= (billAmount * serviceQuality) / numpeople;
	 total =Math.round(total * 100) / 100;
     total = total.toFixed(2);
     // Display the tip!
     document.getElementById("totalTip").style.display = "block";
     document.getElementById("tip").style.innerHTML = total;
 }
	// Hide the tip amount on load
	document.getElementById("totalTip").style.display = "none";
	document.getElementById("each").style.display = "none";
 // Hide the tip amount on load
 document.getElementById("totalTip").style.display="none";
 document.getElementById("each").style.display="none";