document.addEventListener('DOMContentLoaded', function() {
    let display = document.getElementById('display');
    let currentInput = '';

    function updateDisplay(value) {
        display.textContent = value;
    }

    window.appendToDisplay = function(value) {
        if (display.textContent === '0' && value !== '/') {
            currentInput = '';
        }
        currentInput += value;
        updateDisplay(currentInput);
    };

    window.clearDisplay = function() {
        currentInput = '';
        updateDisplay('0');
    };

    window.calculateResult = async function() {
        try {
            const response = await fetch('/calculate', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ expression: currentInput }),
            });
            
            const data = await response.json();
            
            if (response.ok) {
                updateDisplay(data.result);
                currentInput = data.result;
            } else {
                updateDisplay('Error');
                currentInput = '';
            }
        } catch (error) {
            updateDisplay('Error');
            currentInput = '';
        }
    };
});
