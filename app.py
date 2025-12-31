from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from dotenv import load_dotenv
import sqlite3

app = Flask(__name__)
CORS(app)

load_dotenv()

@app.route('/')
def home():
    return {"status": "✅ Medical Chatbot Backend Running!", "env": os.getenv('FLASK_ENV')}

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    message = data.get('message', '')
    
    # Simple medical response (replace with your AI model later)
    responses = {
        "headache": "For headache, rest in dark room, hydrate, paracetamol 500mg every 6hrs. Consult doctor if persists >48hrs.",
        "fever": "Fever: paracetamol 500mg, stay hydrated, rest. Seek medical help if >101°F or lasts >3 days.",
        "cough": "Cough: honey+warm water, steam inhalation. See doctor if blood, chest pain, or >2 weeks."
    }
    
    response = responses.get(message.lower(), "🤖 Medical chatbot active. Please describe symptoms.")
    
    return jsonify({
        'response': response,
        'confidence': 0.95,
        'message': message
    })

if __name__ == '__main__':
    print("✅ Starting Medical Chatbot Backend...")
    print(f"✅ FLASK_ENV: {os.getenv('FLASK_ENV')}")
    print(f"✅ SECRET_KEY: {'LOADED' if os.getenv('SECRET_KEY') else 'MISSING'}")
    app.run(debug=True, host='127.0.0.1', port=5000)
