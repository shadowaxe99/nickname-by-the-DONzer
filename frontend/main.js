```javascript
document.addEventListener('DOMContentLoaded', (event) => {
    const inputField = document.getElementById('inputField');
    const generateButton = document.getElementById('generateButton');
    const outputField = document.getElementById('outputField');
    const shareButton = document.getElementById('shareButton');

    generateButton.addEventListener('click', async () => {
        const userInput = inputField.value;
        let response;
        try {
            response = await fetch('/generate', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ userInput })
            });
        } catch (error) {
            console.error('Error:', error);
        }
        const { generatedNickname, generatedResponse, debateSimulation } = await response.json();
        outputField.textContent = generatedNickname || generatedResponse || debateSimulation;
    });

    shareButton.addEventListener('click', async () => {
        const contentToShare = outputField.textContent;
        try {
            await fetch('/share', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ contentToShare })
            });
            alert('Shared successfully!');
        } catch (error) {
            console.error('Error:', error);
        }
    });
});
```