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
                alert('Please fill all fields with valid values!');
            }
        });
    }
});

// Validate individual input
function validateInput(input) {
    const value = parseFloat(input.value);
    const min = parseFloat(input.min);
    const max = parseFloat(input.max);
    
    if (isNaN(value)) {
        input.style.borderColor = '#e74c3c';
        return false;
    }
    
    if ((min !== null && value < min) || (max !== null && value > max)) {
        input.style.borderColor = '#e74c3c';
        return false;
    }
    
    input.style.borderColor = '#2ecc71';
    return true;
}

// Fill example data
function fillExample() {
    // Example values for Rice crop
    const exampleData = {
        nitrogen: 90,
        phosphorus: 42,
        potassium: 43,
        temperature: 20.87,
        humidity: 82.00,
        ph: 6.50,
        rainfall: 202.93
    };
    
    Object.keys(exampleData).forEach(key => {
        const input = document.getElementById(key);
        if (input) {
            input.value = exampleData[key];
            input.style.borderColor = '#2ecc71';
        }
    });
    
    // Smooth scroll to form
    document.querySelector('.prediction-form').scrollIntoView({ 
        behavior: 'smooth',
        block: 'center'
    });
}

// Add loading animation on form submit
document.addEventListener('DOMContentLoaded', function() {
    const form = document.querySelector('.prediction-form');
    
    if (form) {
        form.addEventListener('submit', function() {
            const submitBtn = form.querySelector('.submit-btn');
            submitBtn.innerHTML = '⏳ Analyzing...';
            submitBtn.disabled = true;
        });
    }
});

// Print functionality enhancement
function printResults() {
    window.print();
}