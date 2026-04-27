/**
 * Project Cloak Access: Web Interface Interactions
 * 
 * Definition:
 * DOM (Document Object Model): A programming interface for web documents. It 
 * represents the page so that programs can change the document structure, style, 
 * and content.
 * 
 * Concepts:
 * 1. Event Listener: A procedure in JavaScript that waits for an event to occur. 
 *    The event could be a user clicking a button, a web page finishing loading, etc.
 * 2. AJAX (Asynchronous JavaScript and XML): A set of web development techniques 
 *    that allows a web page to communicate with a server without reloading the page.
 * 3. Fetch API: A modern interface that allows you to make HTTP requests to servers 
 *    from web browsers.
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
