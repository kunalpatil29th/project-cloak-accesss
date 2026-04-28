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

    // Setup HSV slider value updates
    const sliderIds = [
        'h1-low', 's1-low', 'v1-low',
        'h1-high', 's1-high', 'v1-high',
        'h2-low', 's2-low', 'v2-low',
        'h2-high', 's2-high', 'v2-high'
    ];

    sliderIds.forEach(id => {
        const slider = document.getElementById(id);
        const valSpan = document.getElementById(`${id}-val`);
        if (slider && valSpan) {
            slider.addEventListener('input', () => {
                valSpan.textContent = slider.value;
            });
        }
    });

    // Update HSV button handler
    const updateHsvBtn = document.getElementById('update-hsv-btn');
    if (updateHsvBtn) {
        updateHsvBtn.addEventListener('click', () => {
            const hsvData = {
                h1_low: parseInt(document.getElementById('h1-low').value),
                s1_low: parseInt(document.getElementById('s1-low').value),
                v1_low: parseInt(document.getElementById('v1-low').value),
                h1_high: parseInt(document.getElementById('h1-high').value),
                s1_high: parseInt(document.getElementById('s1-high').value),
                v1_high: parseInt(document.getElementById('v1-high').value),
                h2_low: parseInt(document.getElementById('h2-low').value),
                s2_low: parseInt(document.getElementById('s2-low').value),
                v2_low: parseInt(document.getElementById('v2-low').value),
                h2_high: parseInt(document.getElementById('h2-high').value),
                s2_high: parseInt(document.getElementById('s2-high').value),
                v2_high: parseInt(document.getElementById('v2-high').value)
            };

            fetch('/update_hsv', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(hsvData)
            })
                .then(response => response.json())
                .then(data => {
                    alert(data.message);
                })
                .catch(error => {
                    console.error('Error:', error);
                    alert('Failed to update HSV ranges.');
                });
        });
    }
});
