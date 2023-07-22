document.addEventListener('DOMContentLoaded', function () {
    const activateButton = document.getElementById('activate-button');
    const deactivateButton = document.getElementById('deactivate-button');

    // Function to send POST request to activate or deactivate the pump
    function sendPumpStatus(status) {
        fetch('/detection', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded'
            },
            body: 'value=' + status
        })
        .then(response => {
            if (response.ok) {
                console.log('Pump status updated successfully.');
            } else {
                console.error('Failed to update pump status.');
            }
        })
        .catch(error => {
            console.error('Error:', error);
        });
    }

    // Event listener for the activate button
    activateButton.addEventListener('click', function () {
        sendPumpStatus(1);
    });

    // Event listener for the deactivate button
    deactivateButton.addEventListener('click', function () {
        sendPumpStatus(0);
    });
});
