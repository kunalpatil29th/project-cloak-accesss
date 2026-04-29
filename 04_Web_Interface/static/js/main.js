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
 * 4. Error Handling: The process of catching and managing errors that occur during 
 *    program execution.
 * 5. RGB to HSV Conversion: A color space conversion that transforms red-green-blue 
 *    values to hue-saturation-value for easier color detection.
 */

let notificationTimeout;

function setButtonLoading(button, loading) {
    if (button) {
        button.disabled = loading;
        if (loading) {
            button.classList.add('loading');
        } else {
            button.classList.remove('loading');
        }
    }
}

function showNotification(message, type = 'success') {
    /**
     * Displays a notification to the user.
     * 
     * Definition: Notification System - A component that provides user feedback 
     * about the outcome of operations, without interrupting the user's workflow.
     */
    const notification = document.getElementById('notification');
    if (notification) {
        notification.textContent = message;
        notification.className = `notification ${type}`;
        
        if (notificationTimeout) {
            clearTimeout(notificationTimeout);
        }
        
        notificationTimeout = setTimeout(() => {
            hideNotification();
        }, 5000);
    }
}

function hideNotification() {
    const notification = document.getElementById('notification');
    if (notification) {
        notification.className = 'notification hidden';
    }
}

function hexToRgb(hex) {
    /**
     * Converts hex color to RGB.
     * 
     * Definition: Hexadecimal Color Code - A 6-digit number representing 
     * red, green, and blue components of a color.
     */
    const r = parseInt(hex.slice(1, 3), 16);
    const g = parseInt(hex.slice(3, 5), 16);
    const b = parseInt(hex.slice(5, 7), 16);
    return { r, g, b };
}

function rgbToHsv(r, g, b) {
    /**
     * Converts RGB to HSV (for OpenCV: H 0-179, S 0-255, V 0-255).
     * 
     * Definition: HSV Color Space - A color model that separates color information 
     * into Hue (color type), Saturation (vibrancy), and Value (brightness).
     */
    r /= 255;
    g /= 255;
    b /= 255;
    
    const max = Math.max(r, g, b);
    const min = Math.min(r, g, b);
    let h, s, v = max;
    
    const d = max - min;
    s = max === 0 ? 0 : d / max;
    
    if (max === min) {
        h = 0;
    } else {
        switch (max) {
            case r:
                h = (g - b) / d + (g < b ? 6 : 0);
                break;
            case g:
                h = (b - r) / d + 2;
                break;
            case b:
                h = (r - g) / d + 4;
                break;
        }
        h /= 6;
    }
    
    return {
        h: Math.round(h * 179),
        s: Math.round(s * 255),
        v: Math.round(v * 255)
    };
}

function updateSlider(id, value) {
    const slider = document.getElementById(id);
    const valSpan = document.getElementById(`${id}-val`);
    if (slider && valSpan) {
        slider.value = value;
        valSpan.textContent = value;
    }
}

document.addEventListener('DOMContentLoaded', () => {
    console.log("Project Cloak Access Web Interface Loaded.");

    // Keyboard shortcuts
    document.addEventListener('keydown', (e) => {
        // Ignore if typing in an input field
        if (e.target.tagName === 'INPUT') return;
        
        switch(e.key.toLowerCase()) {
            case 'c':
                // Capture background
                const captureBtn = document.getElementById('capture-btn');
                if (captureBtn) captureBtn.click();
                break;
            case 'u':
                // Update HSV
                const updateHsvBtn = document.getElementById('update-hsv-btn');
                if (updateHsvBtn) updateHsvBtn.click();
                break;
            case '?':
                // Toggle shortcuts section
                const shortcutsSection = document.getElementById('keyboard-shortcuts');
                if (shortcutsSection) {
                    shortcutsSection.style.display = shortcutsSection.style.display === 'none' ? 'block' : 'none';
                }
                break;
        }
    });

    const captureBtn = document.getElementById('capture-btn');
    if (captureBtn) {
        captureBtn.addEventListener('click', () => {
            setButtonLoading(captureBtn, true);
            fetch('/capture_background')
                .then(response => {
                    if (!response.ok) {
                        throw new Error(`HTTP error! Status: ${response.status}`);
                    }
                    return response.json();
                })
                .then(data => {
                    showNotification(data.message, 'success');
                })
                .catch(error => {
                    console.error('Error:', error);
                    showNotification(`Failed to capture background: ${error.message}`, 'error');
                })
                .finally(() => {
                    setButtonLoading(captureBtn, false);
                });
        });
    }

    // Setup HSV slider value updates
    const sliderIds = [
        'h1-low', 's1-low', 'v1-low',
        'h1-high', 's1-high', 'v1-high',
        'h2-low', 's2-low', 'v2-low',
        'h2-high', 's2-high', 'v2-high',
        'kernel-size', 'dilation-iter'
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
            try {
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

                // Validate HSV values
                Object.values(hsvData).forEach(val => {
                    if (isNaN(val)) {
                        throw new Error('All HSV values must be numbers');
                    }
                });

                setButtonLoading(updateHsvBtn, true);
                fetch('/update_hsv', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify(hsvData)
                })
                    .then(response => {
                        if (!response.ok) {
                            throw new Error(`HTTP error! Status: ${response.status}`);
                        }
                        return response.json();
                    })
                    .then(data => {
                        showNotification(data.message, 'success');
                    })
                    .catch(error => {
                        console.error('Error:', error);
                        showNotification(`Failed to update HSV ranges: ${error.message}`, 'error');
                    })
                    .finally(() => {
                        setButtonLoading(updateHsvBtn, false);
                    });
            } catch (error) {
                console.error('Error:', error);
                showNotification(`Validation error: ${error.message}`, 'error');
            }
        });
    }

    // Update Morphology button handler
    const updateMorphBtn = document.getElementById('update-morph-btn');
    if (updateMorphBtn) {
        updateMorphBtn.addEventListener('click', () => {
            try {
                const morphData = {
                    kernel_size: parseInt(document.getElementById('kernel-size').value),
                    dilation_iterations: parseInt(document.getElementById('dilation-iter').value)
                };

                // Validate values
                Object.values(morphData).forEach(val => {
                    if (isNaN(val)) {
                        throw new Error('All morphological parameters must be numbers');
                    }
                });

                setButtonLoading(updateMorphBtn, true);
                fetch('/update_morph', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify(morphData)
                })
                    .then(response => {
                        if (!response.ok) {
                            throw new Error(`HTTP error! Status: ${response.status}`);
                        }
                        return response.json();
                    })
                    .then(data => {
                        showNotification(data.message, 'success');
                    })
                    .catch(error => {
                        console.error('Error:', error);
                        showNotification(`Failed to update morphological parameters: ${error.message}`, 'error');
                    })
                    .finally(() => {
                        setButtonLoading(updateMorphBtn, false);
                    });
            } catch (error) {
                console.error('Error:', error);
                showNotification(`Validation error: ${error.message}`, 'error');
            }
        });
    }

    // Color presets
    const colorPresets = {
        red: { h: 0, hex: '#ff0000' },
        blue: { h: 120, hex: '#0000ff' },
        green: { h: 60, hex: '#00ff00' },
        yellow: { h: 30, hex: '#ffff00' },
        cyan: { h: 90, hex: '#00ffff' },
        magenta: { h: 150, hex: '#ff00ff' }
    };
    
    const presetBtns = document.querySelectorAll('.preset-btn');
    presetBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            const colorName = btn.dataset.color;
            const preset = colorPresets[colorName];
            if (preset) {
                document.getElementById('color-input').value = preset.hex;
                
                // Trigger input event to update preview and HSV display
                const event = new Event('input');
                document.getElementById('color-input').dispatchEvent(event);
            }
        });
    });

    // Color picker functionality
    const colorInput = document.getElementById('color-input');
    const colorPreview = document.getElementById('color-preview');
    const pickerH = document.getElementById('picker-h');
    const pickerS = document.getElementById('picker-s');
    const pickerV = document.getElementById('picker-v');
    const applyColorBtn = document.getElementById('apply-color-btn');
    
    if (colorInput && colorPreview && pickerH && pickerS && pickerV) {
        // Initialize preview
        colorPreview.style.backgroundColor = colorInput.value;
        
        colorInput.addEventListener('input', () => {
            const hex = colorInput.value;
            colorPreview.style.backgroundColor = hex;
            
            const rgb = hexToRgb(hex);
            const hsv = rgbToHsv(rgb.r, rgb.g, rgb.b);
            
            pickerH.textContent = hsv.h;
            pickerS.textContent = Math.round((hsv.s / 255) * 100);
            pickerV.textContent = Math.round((hsv.v / 255) * 100);
        });
        
        if (applyColorBtn) {
            applyColorBtn.addEventListener('click', () => {
                const hex = colorInput.value;
                const rgb = hexToRgb(hex);
                const hsv = rgbToHsv(rgb.r, rgb.g, rgb.b);
                
                // Calculate ranges around the selected color
                const toleranceH = 10;
                const toleranceS = 50;
                const toleranceV = 50;
                
                let hLow = Math.max(0, hsv.h - toleranceH);
                let hHigh = Math.min(179, hsv.h + toleranceH);
                const sLow = Math.max(0, hsv.s - toleranceS);
                const sHigh = Math.min(255, hsv.s + toleranceS);
                const vLow = Math.max(0, hsv.v - toleranceV);
                const vHigh = Math.min(255, hsv.v + toleranceV);
                
                // Handle red's two ranges (wraps around 180)
                if (hLow < 0) {
                    updateSlider('h1-low', 179 + hLow);
                    updateSlider('h1-high', 179);
                    updateSlider('h2-low', 0);
                    updateSlider('h2-high', hHigh);
                } else if (hHigh > 179) {
                    updateSlider('h1-low', hLow);
                    updateSlider('h1-high', 179);
                    updateSlider('h2-low', 0);
                    updateSlider('h2-high', hHigh - 179);
                } else {
                    // Single range, set both to same values for simplicity
                    updateSlider('h1-low', hLow);
                    updateSlider('h1-high', hHigh);
                    updateSlider('h2-low', hLow);
                    updateSlider('h2-high', hHigh);
                }
                
                updateSlider('s1-low', sLow);
                updateSlider('s1-high', sHigh);
                updateSlider('s2-low', sLow);
                updateSlider('s2-high', sHigh);
                updateSlider('v1-low', vLow);
                updateSlider('v1-high', vHigh);
                updateSlider('v2-low', vLow);
                updateSlider('v2-high', vHigh);
                
                showNotification('Color applied to sliders!', 'success');
            });
        }
    }

    // Recording controls
    const startRecordBtn = document.getElementById('start-record-btn');
    const stopRecordBtn = document.getElementById('stop-record-btn');
    const downloadBtn = document.getElementById('download-btn');
    
    if (startRecordBtn && stopRecordBtn) {
        startRecordBtn.addEventListener('click', () => {
            setButtonLoading(startRecordBtn, true);
            fetch('/start_recording', {
                method: 'POST'
            })
                .then(response => {
                    if (!response.ok) {
                        throw new Error(`HTTP error! Status: ${response.status}`);
                    }
                    return response.json();
                })
                .then(data => {
                    showNotification(data.message, 'success');
                    startRecordBtn.style.display = 'none';
                    stopRecordBtn.style.display = 'inline-block';
                })
                .catch(error => {
                    console.error('Error:', error);
                    showNotification(`Failed to start recording: ${error.message}`, 'error');
                })
                .finally(() => {
                    setButtonLoading(startRecordBtn, false);
                });
        });
        
        stopRecordBtn.addEventListener('click', () => {
            setButtonLoading(stopRecordBtn, true);
            fetch('/stop_recording', {
                method: 'POST'
            })
                .then(response => {
                    if (!response.ok) {
                        throw new Error(`HTTP error! Status: ${response.status}`);
                    }
                    return response.json();
                })
                .then(data => {
                    showNotification(data.message, 'success');
                    stopRecordBtn.style.display = 'none';
                    startRecordBtn.style.display = 'inline-block';
                })
                .catch(error => {
                    console.error('Error:', error);
                    showNotification(`Failed to stop recording: ${error.message}`, 'error');
                })
                .finally(() => {
                    setButtonLoading(stopRecordBtn, false);
                });
        });
    }
    
    if (downloadBtn) {
        downloadBtn.addEventListener('click', () => {
            window.location.href = '/download';
        });
    }

    // Delete session functionality
    const deleteBtns = document.querySelectorAll('.delete-btn');
    deleteBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            const sessionId = btn.dataset.sessionId;
            if (confirm(`Are you sure you want to delete session ${sessionId}?`)) {
                setButtonLoading(btn, true);
                fetch(`/delete_session/${sessionId}`, {
                    method: 'DELETE'
                })
                    .then(response => {
                        if (!response.ok) {
                            throw new Error(`HTTP error! Status: ${response.status}`);
                        }
                        return response.json();
                    })
                    .then(data => {
                        showNotification(data.message, 'success');
                        // Remove the row from the table
                        const row = document.querySelector(`tr[data-session-id="${sessionId}"]`);
                        if (row) {
                            row.remove();
                        }
                    })
                    .catch(error => {
                        console.error('Error:', error);
                        showNotification(`Failed to delete session: ${error.message}`, 'error');
                    })
                    .finally(() => {
                        setButtonLoading(btn, false);
                    });
            }
        });
    });

    // Clear history functionality
    const clearHistoryBtn = document.getElementById('clear-history-btn');
    if (clearHistoryBtn) {
        clearHistoryBtn.addEventListener('click', () => {
            if (confirm('Are you sure you want to clear all history? This cannot be undone!')) {
                setButtonLoading(clearHistoryBtn, true);
                fetch('/clear_history', {
                    method: 'DELETE'
                })
                    .then(response => {
                        if (!response.ok) {
                            throw new Error(`HTTP error! Status: ${response.status}`);
                        }
                        return response.json();
                    })
                    .then(data => {
                        showNotification(data.message, 'success');
                        // Remove all rows from the table
                        const tbody = document.querySelector('tbody');
                        if (tbody) {
                            tbody.innerHTML = '';
                        }
                    })
                    .catch(error => {
                        console.error('Error:', error);
                        showNotification(`Failed to clear history: ${error.message}`, 'error');
                    })
                    .finally(() => {
                        setButtonLoading(clearHistoryBtn, false);
                    });
            }
        });
    }
});
