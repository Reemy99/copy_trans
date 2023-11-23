
document.addEventListener('DOMContentLoaded', function() {
  const playNowBtn = document.getElementById('playNowBtn');
  const otherElement = document.getElementById('otherElement');

  playNowBtn.addEventListener('click', function() {
      fetch('button1.html')
          .then(response => response.text())
          .then(data => {
              otherElement.innerHTML = data;
              playNowBtn.style.display = 'none'; // Hide the button
              otherElement.style.display = 'block'; // Show the loaded content
          })
          .catch(error => console.log(error));
  });
});
