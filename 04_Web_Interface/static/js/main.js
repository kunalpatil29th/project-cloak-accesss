/**
 * Project Cloak Access: Web Interface Interactions
 */

document.addEventListener('DOMContentLoaded', () => {
    console.log("Project Cloak Access Web Interface Loaded.");

    const captureBtn = document.getElementById('capture-btn');
    if (captureBtn) {
        captureBtn.addEventListener('click', () => {
            fetch('/capture_background')
                .then(response => response.json())
                .then(data => {
                    alert(data.message);
                })
                .catch(error => {
                    console.error('Error:', error);
                    alert('Failed to capture background.');
                });
        });
    }
});
