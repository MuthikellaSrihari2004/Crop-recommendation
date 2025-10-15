from flask import Flask, render_template, request, jsonify
import joblib
import numpy as np
import os

app = Flask(__name__)

# Load models
MODEL_PATH = 'models/crop_model.pkl'
SCALER_PATH = 'models/scaler.pkl'
LABEL_ENCODER_PATH = 'models/label_encoder.pkl'

# Global variables to store models
model = None
scaler = None
label_encoder = None

def load_models():
    """Load all trained models"""
    global model, scaler, label_encoder
    
    try:
        if os.path.exists(MODEL_PATH):
            model = joblib.load(MODEL_PATH)
            scaler = joblib.load(SCALER_PATH)
            label_encoder = joblib.load(LABEL_ENCODER_PATH)
            print("Models loaded successfully!")
            return True
        else:
            print("Models not found. Please train the model first by running model.py")
            return False
    except Exception as e:
        print(f"Error loading models: {str(e)}")
        return False

# Load models when app starts
models_loaded = load_models()

# Crop information dictionary
CROP_INFO = {
    'rice': {
        'description': 'Rice is a staple food crop that grows well in warm, humid conditions with abundant water.',
        'season': 'Kharif (Monsoon)',
        'duration': '3-6 months'
    },
    'wheat': {
        'description': 'Wheat is a cereal grain that thrives in cooler climates with moderate rainfall.',
        'season': 'Rabi (Winter)',
        'duration': '4-6 months'
    },
    'maize': {
        'description': 'Maize (corn) is versatile and can grow in various climates with adequate moisture.',
        'season': 'Kharif & Rabi',
        'duration': '3-4 months'
    },
    'chickpea': {
        'description': 'Chickpea is a protein-rich legume that grows in cool, dry conditions.',
        'season': 'Rabi (Winter)',
        'duration': '4-5 months'
    },
    'kidneybeans': {
        'description': 'Kidney beans are nutritious legumes that prefer warm temperatures.',
        'season': 'Kharif',
        'duration': '3-4 months'
    },
    'pigeonpeas': {
        'description': 'Pigeon peas are drought-tolerant legumes suitable for semi-arid regions.',
        'season': 'Kharif',
        'duration': '5-7 months'
    },
    'mothbeans': {
        'description': 'Moth beans are drought-resistant legumes ideal for arid conditions.',
        'season': 'Kharif',
        'duration': '3-4 months'
    },
    'mungbean': {
        'description': 'Mung beans are fast-growing legumes rich in protein.',
        'season': 'Kharif & Summer',
        'duration': '2-3 months'
    },
    'blackgram': {
        'description': 'Black gram is a pulse crop that grows well in warm, humid conditions.',
        'season': 'Kharif & Rabi',
        'duration': '3-4 months'
    },
    'lentil': {
        'description': 'Lentils are cool-season legumes that prefer moderate temperatures.',
        'season': 'Rabi (Winter)',
        'duration': '4-5 months'
    },
    'pomegranate': {
        'description': 'Pomegranate is a fruit crop that thrives in semi-arid climates.',
        'season': 'Year-round',
        'duration': 'Perennial'
    },
    'banana': {
        'description': 'Banana requires warm, humid conditions with consistent moisture.',
        'season': 'Year-round',
        'duration': '9-12 months'
    },
    'mango': {
        'description': 'Mango is a tropical fruit that needs hot, dry weather for fruit development.',
        'season': 'Year-round (fruit in summer)',
        'duration': 'Perennial'
    },
    'grapes': {
        'description': 'Grapes grow best in warm, dry climates with moderate rainfall.',
        'season': 'Year-round',
        'duration': 'Perennial'
    },
    'watermelon': {
        'description': 'Watermelon is a warm-season crop that needs plenty of sun and water.',
        'season': 'Summer',
        'duration': '2-3 months'
    },
    'muskmelon': {
        'description': 'Muskmelon grows well in warm weather with good drainage.',
        'season': 'Summer',
        'duration': '2-3 months'
    },
    'apple': {
        'description': 'Apples require cool winters and moderate summers for optimal growth.',
        'season': 'Year-round (fruit in autumn)',
        'duration': 'Perennial'
    },
    'orange': {
        'description': 'Oranges thrive in subtropical climates with mild winters.',
        'season': 'Year-round',
        'duration': 'Perennial'
    },
    'papaya': {
        'description': 'Papaya grows best in tropical and subtropical regions.',
        'season': 'Year-round',
        'duration': '9-12 months'
    },
    'coconut': {
        'description': 'Coconut palms thrive in coastal tropical regions with high humidity.',
        'season': 'Year-round',
        'duration': 'Perennial'
    },
    'cotton': {
        'description': 'Cotton requires warm weather and moderate rainfall.',
        'season': 'Kharif',
        'duration': '5-6 months'
    },
    'jute': {
        'description': 'Jute needs warm, humid conditions with heavy rainfall.',
        'season': 'Kharif',
        'duration': '4-5 months'
    },
    'coffee': {
        'description': 'Coffee grows in tropical highlands with consistent temperatures.',
        'season': 'Year-round',
        'duration': 'Perennial'
    }
}

@app.route('/')
def home():
    """Render home page"""
    return render_template('index.html', models_loaded=models_loaded)

@app.route('/predict', methods=['POST'])
def predict():
    """Handle prediction requests"""
    if not models_loaded:
        return jsonify({
            'error': 'Models not loaded. Please train the model first.'
        }), 500
    
    try:
        # Get form data
        N = float(request.form['nitrogen'])
        P = float(request.form['phosphorus'])
        K = float(request.form['potassium'])
        temperature = float(request.form['temperature'])
        humidity = float(request.form['humidity'])
        ph = float(request.form['ph'])
        rainfall = float(request.form['rainfall'])
        
        # Validate inputs
        if not (0 <= N <= 200 and 0 <= P <= 200 and 0 <= K <= 200):
            return render_template('result.html', 
                                 error="Nutrient values should be between 0 and 200")
        
        if not (0 <= temperature <= 50):
            return render_template('result.html', 
                                 error="Temperature should be between 0°C and 50°C")
        
        if not (0 <= humidity <= 100):
            return render_template('result.html', 
                                 error="Humidity should be between 0% and 100%")
        
        if not (0 <= ph <= 14):
            return render_template('result.html', 
                                 error="pH should be between 0 and 14")
        
        if rainfall < 0:
            return render_template('result.html', 
                                 error="Rainfall cannot be negative")
        
        # Prepare input data
        input_data = np.array([[N, P, K, temperature, humidity, ph, rainfall]])
        
        # Scale the input
        input_scaled = scaler.transform(input_data)
        
        # Make prediction
        prediction = model.predict(input_scaled)
        prediction_proba = model.predict_proba(input_scaled)
        
        # Get crop name
        crop_name = label_encoder.inverse_transform(prediction)[0]
        confidence = np.max(prediction_proba) * 100
        
        # Get top 3 predictions
        top_3_indices = np.argsort(prediction_proba[0])[-3:][::-1]
        top_3_crops = label_encoder.inverse_transform(top_3_indices)
        top_3_probabilities = prediction_proba[0][top_3_indices] * 100
        
        alternatives = [
            {'name': crop, 'confidence': f"{prob:.2f}"}
            for crop, prob in zip(top_3_crops[1:], top_3_probabilities[1:])
        ]
        
        # Get crop information
        crop_details = CROP_INFO.get(crop_name.lower(), {
            'description': 'A suitable crop for your soil and climate conditions.',
            'season': 'Varies',
            'duration': 'Varies'
        })
        
        return render_template('result.html',
                             crop=crop_name.title(),
                             confidence=f"{confidence:.2f}",
                             alternatives=alternatives,
                             description=crop_details['description'],
                             season=crop_details['season'],
                             duration=crop_details['duration'],
                             inputs={
                                 'Nitrogen': N,
                                 'Phosphorus': P,
                                 'Potassium': K,
                                 'Temperature': temperature,
                                 'Humidity': humidity,
                                 'pH': ph,
                                 'Rainfall': rainfall
                             })
    
    except ValueError:
        return render_template('result.html', 
                             error="Please enter valid numeric values")
    except Exception as e:
        return render_template('result.html', 
                             error=f"An error occurred: {str(e)}")

@app.route('/api/predict', methods=['POST'])
def api_predict():
    """API endpoint for predictions"""
    if not models_loaded:
        return jsonify({
            'error': 'Models not loaded. Please train the model first.'
        }), 500
    
    try:
        data = request.get_json()
        
        # Prepare input
        input_data = np.array([[
            data['N'], data['P'], data['K'],
            data['temperature'], data['humidity'],
            data['ph'], data['rainfall']
        ]])
        
        # Scale and predict
        input_scaled = scaler.transform(input_data)
        prediction = model.predict(input_scaled)
        prediction_proba = model.predict_proba(input_scaled)
        
        # Get results
        crop_name = label_encoder.inverse_transform(prediction)[0]
        confidence = float(np.max(prediction_proba) * 100)
        
        return jsonify({
            'crop': crop_name,
            'confidence': confidence,
            'status': 'success'
        })
    
    except Exception as e:
        return jsonify({
            'error': str(e),
            'status': 'error'
        }), 400

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)