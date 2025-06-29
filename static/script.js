document.getElementById('runBtn').addEventListener('click', () => {
  fetch('/run-script')
    .then(response => response.json())
    .then(data => {
      if (data.output) {
        document.getElementById('output').textContent = data.output;
      } else {
        document.getElementById('output').textContent = data.error;
      }
    })
    .catch(err => {
      document.getElementById('output').textContent = err;
    });
});
