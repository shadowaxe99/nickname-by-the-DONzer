```python
from flask import Flask, request, jsonify
from ai_models import gpt3_model, codex_model
from social_media_integration import shareOnSocialMedia
from database import saveNickname
from utils import generateNickname, generateResponse, simulateDebate

app = Flask(__name__)

@app.route('/generateNickname', methods=['POST'])
def generate_nickname():
    userInput = request.json['userInput']
    generatedNickname = generateNickname(userInput, gpt3_model)
    return jsonify({'nickname': generatedNickname})

@app.route('/generateResponse', methods=['POST'])
def generate_response():
    userInput = request.json['userInput']
    generatedResponse = generateResponse(userInput, gpt3_model)
    return jsonify({'response': generatedResponse})

@app.route('/simulateDebate', methods=['POST'])
def simulate_debate():
    userInput = request.json['userInput']
    debateSimulation = simulateDebate(userInput, gpt3_model)
    return jsonify({'debate': debateSimulation})

@app.route('/shareOnSocialMedia', methods=['POST'])
def share_on_social_media():
    content = request.json['content']
    platform = request.json['platform']
    shareOnSocialMedia(content, platform)
    return jsonify({'status': 'Shared successfully'})

@app.route('/saveNickname', methods=['POST'])
def save_nickname():
    nickname = request.json['nickname']
    saveNickname(nickname)
    return jsonify({'status': 'Saved successfully'})

if __name__ == '__main__':
    app.run(debug=True)
```