// Function to open the popup
function openPopup() {
  var popup = document.getElementById("popup");
  popup.style.display = "block";
}

// Function to close the popup
function closePopup() {
  var popup = document.getElementById("popup");
  popup.style.display = "none";
}

// Function to submit the code (for demonstration purposes)
function submitCode() {
  var code = document.getElementById("validationCode").value;
  if (code.length === 6) {
    // Send the code to the backend or perform validation
    alert("Validation code submitted: " + code);
    closePopup(); // Close the popup after submission (you may adjust this based on your logic)
  } else {
    alert("Please enter a 6-digit code.");
  }
}
