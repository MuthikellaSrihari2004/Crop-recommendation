// Form validation and enhancement
document.addEventListener('DOMContentLoaded', function() {
    const form = document.querySelector('.prediction-form');
    
    if (form) {
        // Add input validation
        const inputs = form.querySelectorAll('input[type="number"]');
        
        inputs.forEach(input => {
            input.addEventListener('input', function() {
                validateInput(this);
            });
            
            // Add focus effects
            input.addEventListener('focus', function() {
                this.parentElement.style.transform = 'scale(1.02)';
                this.parentElement.style.transition = 'transform 0.2s ease';
            });
            
            input.addEventListener('blur', function() {
                this.parentElement.style.transform = 'scale(1)';
            });
        });
        
        // Form submission
        form.addEventListener('submit', function(e) {
            let isValid = true;
            
            inputs.forEach(input => {
                if (!validateInput(input)) {
                    isValid = false;
                }
            });
            
            if (!isValid) {
                e.preventDefault();
                showNotification('⚠️ Please fill all fields with valid values!', 'error');
            }
        });
    }
});

// Validate individual input
function validateInput(input) {
    const value = parseFloat(input.value);
    const min = parseFloat(input.min);
    const max = parseFloat(input.max);
    
    if (isNaN(value) || input.value.trim() === '') {
        input.style.borderColor = '#e74c3c';
        input.style.backgroundColor = '#ffe6e6';
        return false;
    }
    
    if ((min !== null && value < min) || (max !== null && value > max)) {
        input.style.borderColor = '#f39c12';
        input.style.backgroundColor = '#fff3cd';
        return false;
    }
    
    input.style.borderColor = '#2ecc71';
    input.style.backgroundColor = '#f0fff4';
    return true;
}

// Fill example data with different crop types
function fillExample(cropType = 'rice') {
    // Example values for different crops
    const exampleData = {
        'rice': {
            nitrogen: 90,
            phosphorus: 42,
            potassium: 43,
            temperature: 20.87,
            humidity: 82.00,
            ph: 6.50,
            rainfall: 202.93
        },
        'cotton': {
            nitrogen: 120,
            phosphorus: 50,
            potassium: 50,
            temperature: 25.00,
            humidity: 80.00,
            ph: 7.20,
            rainfall: 85.00
        },
        'maize': {
            nitrogen: 80,
            phosphorus: 55,
            potassium: 48,
            temperature: 23.00,
            humidity: 65.00,
            ph: 6.80,
            rainfall: 95.00
        }
    };
    
    const data = exampleData[cropType] || exampleData['rice'];
    
    // Fill form fields with animation
    Object.keys(data).forEach((key, index) => {
        const input = document.getElementById(key);
        if (input) {
            setTimeout(() => {
                input.value = data[key];
                input.style.borderColor = '#2ecc71';
                input.style.transition = 'all 0.3s ease';
                input.style.backgroundColor = '#e8f5e9';
                
                // Validate the input
                validateInput(input);
                
                // Add pulse animation
                input.classList.add('pulse-animation');
                setTimeout(() => {
                    input.style.backgroundColor = '#f0fff4';
                    input.classList.remove('pulse-animation');
                }, 600);
            }, index * 100); // Stagger the animation
        }
    });
    
    // Smooth scroll to form
    setTimeout(() => {
        document.querySelector('.prediction-form').scrollIntoView({ 
            behavior: 'smooth',
            block: 'center'
        });
    }, 200);
    
    // Show notification
    const cropNames = {
        'rice': 'Rice 🌾',
        'wheat': 'Wheat 🌾',
        'cotton': 'Cotton ☁️',
        'maize': 'Maize 🌽'
    };
    
    showNotification(`${cropNames[cropType]} example data loaded successfully! ✓`, 'success');
}

// Show notification function
function showNotification(message, type = 'success') {
    // Remove existing notification if any
    const existing = document.querySelector('.notification');
    if (existing) {
        existing.remove();
    }
    
    // Determine colors based on type
    const colors = {
        success: {
            bg: '#2ecc71',
            icon: '✓'
        },
        error: {
            bg: '#e74c3c',
            icon: '✗'
        },
        warning: {
            bg: '#f39c12',
            icon: '⚠'
        },
        info: {
            bg: '#3498db',
            icon: 'ℹ'
        }
    };
    
    const style = colors[type] || colors.success;
    
    // Create notification
    const notification = document.createElement('div');
    notification.className = 'notification';
    notification.innerHTML = `<span class="notification-icon">${style.icon}</span> ${message}`;
    notification.style.cssText = `
        position: fixed;
        top: 20px;
        right: 20px;
        background: ${style.bg};
        color: white;
        padding: 15px 25px;
        border-radius: 8px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.2);
        z-index: 10000;
        animation: slideIn 0.4s ease;
        font-weight: 600;
        font-size: 0.95rem;
        display: flex;
        align-items: center;
        gap: 10px;
        max-width: 400px;
    `;
    
    document.body.appendChild(notification);
    
    // Auto remove after 4 seconds
    setTimeout(() => {
        notification.style.animation = 'slideOut 0.4s ease';
        setTimeout(() => notification.remove(), 400);
    }, 4000);
}

// Add loading animation on form submit
document.addEventListener('DOMContentLoaded', function() {
    const form = document.querySelector('.prediction-form');
    
    if (form) {
        form.addEventListener('submit', function(e) {
            const submitBtn = form.querySelector('.submit-btn');
            const originalText = submitBtn.innerHTML;
            
            submitBtn.innerHTML = '<span class="spinner"></span> Analyzing your data...';
            submitBtn.disabled = true;
            submitBtn.style.opacity = '0.8';
            submitBtn.style.cursor = 'not-allowed';
            
            // Add spinner styles dynamically
            if (!document.getElementById('spinner-styles')) {
                const style = document.createElement('style');
                style.id = 'spinner-styles';
                style.textContent = `
                    .spinner {
                        display: inline-block;
                        width: 16px;
                        height: 16px;
                        border: 3px solid rgba(255,255,255,0.3);
                        border-top-color: white;
                        border-radius: 50%;
                        animation: spin 0.8s linear infinite;
                    }
                    @keyframes spin {
                        to { transform: rotate(360deg); }
                    }
                `;
                document.head.appendChild(style);
            }
        });
    }
});

// Add pulse animation styles
if (!document.getElementById('pulse-styles')) {
    const style = document.createElement('style');
    style.id = 'pulse-styles';
    style.textContent = `
        .pulse-animation {
            animation: pulse 0.6s ease;
        }
        @keyframes pulse {
            0%, 100% { transform: scale(1); }
            50% { transform: scale(1.05); }
        }
    `;
    document.head.appendChild(style);
}

// Print functionality enhancement
function printResults() {
    window.print();
}

// Clear form function (optional - can be added as a button)
function clearForm() {
    const form = document.querySelector('.prediction-form');
    if (form) {
        form.reset();
        const inputs = form.querySelectorAll('input[type="number"]');
        inputs.forEach(input => {
            input.style.borderColor = '#ddd';
            input.style.backgroundColor = '';
        });
        showNotification('Form cleared! 🗑️', 'info');
    }
}

// Keyboard shortcuts
document.addEventListener('keydown', function(e) {
    // Ctrl/Cmd + K to clear form
    if ((e.ctrlKey || e.metaKey) && e.key === 'k') {
        e.preventDefault();
        clearForm();
    }
    
    // Ctrl/Cmd + 1-4 for quick example loading
    if ((e.ctrlKey || e.metaKey) && e.key >= '1' && e.key <= '4') {
        e.preventDefault();
        const crops = ['rice', 'wheat', 'cotton', 'maize'];
        fillExample(crops[parseInt(e.key) - 1]);
    }
});

// Add tooltips on hover (optional enhancement)
document.addEventListener('DOMContentLoaded', function() {
    const inputs = document.querySelectorAll('input[type="number"]');
    
    inputs.forEach(input => {
        input.addEventListener('mouseenter', function() {
            const label = this.previousElementSibling?.textContent || '';
            const min = this.min;
            const max = this.max;
            
            if (min && max) {
                this.title = `Valid range: ${min} to ${max}`;
            }
        });
    });
});

// Auto-save form data to prevent loss (uses browser memory only)
let formDataBackup = {};

document.addEventListener('DOMContentLoaded', function() {
    const form = document.querySelector('.prediction-form');
    
    if (form) {
        const inputs = form.querySelectorAll('input[type="number"]');
        
        // Auto-save on input
        inputs.forEach(input => {
            input.addEventListener('input', function() {
                formDataBackup[this.id] = this.value;
            });
        });
        
        // Restore on page load if data exists
        if (Object.keys(formDataBackup).length > 0) {
            inputs.forEach(input => {
                if (formDataBackup[input.id]) {
                    input.value = formDataBackup[input.id];
                    validateInput(input);
                }
            });
        }
    }
});

// Smooth scroll for all internal links
document.addEventListener('DOMContentLoaded', function() {
    const links = document.querySelectorAll('a[href^="#"]');
    
    links.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });
});

// Console welcome message
console.log('%c🌾 Crop Recommendation System', 'color: #2ecc71; font-size: 20px; font-weight: bold;');
console.log('%cKeyboard Shortcuts:', 'color: #3498db; font-size: 14px; font-weight: bold;');
console.log('Ctrl/Cmd + K: Clear form');
console.log('Ctrl/Cmd + 1: Load Rice example');
console.log('Ctrl/Cmd + 2: Load Wheat example');
console.log('Ctrl/Cmd + 3: Load Cotton example');
console.log('Ctrl/Cmd + 4: Load Maize example');