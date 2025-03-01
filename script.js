document.getElementById('emailForm').addEventListener('submit', function(event) {
    event.preventDefault();

    const recipientName = document.getElementById('recipientName').value;
    const emailType = document.getElementById('emailType').value;
    const additionalInfo = document.getElementById('additionalInfo').value;

    // Prepare data to send to backend (if you have a back-end API)
    const data = {
        recipientName: recipientName,
        emailType: emailType,
        additionalInfo: additionalInfo
    };

    // If you have a backend, use fetch to send the data
    fetch('http://localhost:5000/generate-email', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('generatedEmail').textContent = data.email;
    })
    .catch(error => {
        console.error('Error:', error);
    });
});