# 🌾 Crop Recommendation System

A machine learning-based web application that recommends the most suitable crop to grow based on soil nutrients and environmental conditions.

## 📋 Features

- **Smart Predictions**: Uses Random Forest Classifier for accurate crop recommendations
- **User-Friendly Interface**: Clean and intuitive web interface
- **Real-Time Analysis**: Instant crop suggestions based on input parameters
- **Detailed Results**: Provides confidence scores, alternative crops, and growing information
- **Input Validation**: Ensures data quality with built-in validation
- **Responsive Design**: Works seamlessly on desktop and mobile devices

## 🛠️ Technologies Used

- **Backend**: Python, Flask
- **Machine Learning**: Scikit-learn (Random Forest Classifier)
- **Data Processing**: Pandas, NumPy
- **Frontend**: HTML5, CSS3, JavaScript
- **Model Persistence**: Joblib

## 📁 Project Structure

```
crop-recommendation-system/
│
├── app.py                          # Flask application
├── model.py                        # ML model training script
├── requirements.txt                # Python dependencies
├── README.md                       # Project documentation
│
├── data/
│   └── Crop_recommendation.csv     # Dataset (to be added)
│
├── models/
│   ├── crop_model.pkl             # Trained model (generated)
│   ├── scaler.pkl                 # Feature scaler (generated)
│   └── label_encoder.pkl          # Label encoder (generated)
│
├── templates/
│   ├── index.html                 # Home page
│   └── result.html                # Result page
│
└── static/
    ├── css/
    │   └── style.css              # Stylesheet
    └── js/
        └── script.js              # JavaScript
```

## 🚀 Installation & Setup

### Prerequisites

- Python 3.7 or higher
- pip (Python package manager)

### Step 1: Clone or Create Project Directory

```bash
# Create project directory
mkdir crop-recommendation-system
cd crop-recommendation-system
```

### Step 2: Create Project Structure

Create all the folders:

```bash
mkdir data models templates static
mkdir static/css static/js
```

### Step 3: Add All Project Files

Copy all the files provided into their respective directories:
- `app.py` in root directory
- `model.py` in root directory
- `requirements.txt` in root directory
- `index.html` in `templates/` folder
- `result.html` in `templates/` folder
- `style.css` in `static/css/` folder
- `script.js` in `static/js/` folder

### Step 4: Download Dataset

Download the Crop Recommendation dataset and place it in the `data/` folder:

**Option 1: Kaggle Dataset**
```bash
# Download from: https://www.kaggle.com/datasets/atharvaingle/crop-recommendation-dataset
# Save as: data/Crop_recommendation.csv
```

**Option 2: Create Sample Dataset (for testing)**

If you don't have the dataset, create a sample CSV file manually in `data/Crop_recommendation.csv` with these columns:
```
N,P,K,temperature,humidity,ph,rainfall,label
90,42,43,20.87,82.00,6.50,202.93,rice
85,58,41,21.77,80.31,7.03,226.65,rice
60,55,44,23.00,82.32,7.84,263.96,rice
...
```

### Step 5: Create Virtual Environment (Recommended)

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### Step 6: Install Dependencies

```bash
pip install -r requirements.txt
```

## 🎯 Usage

### Step 1: Train the Machine Learning Model

Before running the application, you need to train the model:

```bash
python model.py
```

This will:
- Load the dataset from `data/Crop_recommendation.csv`
- Preprocess the data
- Train a Random Forest Classifier
- Save the trained model and preprocessors to the `models/` folder
- Display training accuracy and feature importance

**Expected Output:**
```
Loading dataset...
Dataset shape: (2200, 8)
...
Training Random Forest model...
Model training completed!
Accuracy: 99.32%
...
Models saved successfully!
```

### Step 2: Run the Flask Application

```bash
python app.py
```

The application will start on `http://localhost:5000` or `http://127.0.0.1:5000`

**Expected Output:**
```
Models loaded successfully!
 * Running on http://127.0.0.1:5000
 * Debug mode: on
```

### Step 3: Access the Application

Open your web browser and navigate to:
```
http://localhost:5000
```

### Step 4: Make Predictions

1. Fill in the soil and environmental parameters:
   - **Nitrogen (N)**: 0-200 kg/ha
   - **Phosphorus (P)**: 0-200 kg/ha
   - **Potassium (K)**: 0-200 kg/ha
   - **Temperature**: 0-50°C
   - **Humidity**: 0-100%
   - **pH Level**: 0-14
   - **Rainfall**: Annual rainfall in mm

2. Click "Get Crop Recommendation"

3. View your results with:
   - Recommended crop
   - Confidence score
   - Alternative crops
   - Growing information

## 📊 Dataset Information

The dataset should contain the following features:

| Feature | Description | Range |
|---------|-------------|-------|
| N | Nitrogen content | 0-200 kg/ha |
| P | Phosphorus content | 0-200 kg/ha |
| K | Potassium content | 0-200 kg/ha |
| temperature | Temperature | 0-50°C |
| humidity | Relative humidity | 0-100% |
| ph | pH value of soil | 0-14 |
| rainfall | Annual rainfall | mm |
| label | Crop type | (Target variable) |

**Supported Crops** (22 types):
- Rice, Maize, Chickpea, Kidney Beans, Pigeon Peas
- Moth Beans, Mung Bean, Black Gram, Lentil, Pomegranate
- Banana, Mango, Grapes, Watermelon, Muskmelon
- Apple, Orange, Papaya, Coconut, Cotton, Jute, Coffee

## 🔧 Configuration

### Modify Model Parameters

Edit `model.py` to change Random Forest parameters:

```python
model = RandomForestClassifier(
    n_estimators=100,      # Number of trees
    max_depth=20,          # Maximum depth
    min_samples_split=5,   # Minimum samples to split
    min_samples_leaf=2,    # Minimum samples per leaf
    random_state=42
)
```

### Change Server Port

Edit `app.py`:

```python
app.run(debug=True, host='0.0.0.0', port=5000)  # Change port here
```

## 📈 Model Performance

The Random Forest model typically achieves:
- **Accuracy**: 95-99%
- **Training Time**: 2-5 seconds
- **Prediction Time**: <100ms

## 🐛 Troubleshooting

### Issue: Models not loaded error

**Solution:**
```bash
python model.py  # Train the model first
```

### Issue: Dataset not found

**Solution:**
- Ensure `Crop_recommendation.csv` is in the `data/` folder
- Check file name spelling (case-sensitive)

### Issue: Module not found

**Solution:**
```bash
pip install -r requirements.txt
```

### Issue: Port already in use

**Solution:**
```bash
# Change port in app.py or kill the process using the port
# Windows:
netstat -ano | findstr :5000
taskkill /PID <PID> /F
# Linux/macOS:
lsof -ti:5000 | xargs kill -9
```

## 🌐 API Endpoint

The application also provides a REST API endpoint:

```bash
POST /api/predict
Content-Type: application/json

{
    "N": 90,
    "P": 42,
    "K": 43,
    "temperature": 20.87,
    "humidity": 82.00,
    "ph": 6.50,
    "rainfall": 202.93
}
```

**Response:**
```json
{
    "crop": "rice",
    "confidence": 98.50,
    "status": "success"
}
```

## 📝 Example Usage

### Example 1: Rice
```
Nitrogen: 90
Phosphorus: 42
Potassium: 43
Temperature: 20.87°C
Humidity: 82%
pH: 6.5
Rainfall: 202.93mm
→ Result: Rice (98.5% confidence)
```

### Example 2: Maize
```
Nitrogen: 78
Phosphorus: 55
Potassium: 48
Temperature: 23°C
Humidity: 65%
pH: 6.8
Rainfall: 95mm
→ Result: Maize
```

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Submit pull requests

## 📄 License

This project is open-source and available for educational purposes.

## 👨‍💻 Author

Created as an intermediate-level machine learning project demonstrating:
- End-to-end ML pipeline
- Web application development
- Model deployment with Flask
- User interface design

## 🔮 Future Enhancements

- [ ] Add more ML models (SVM, XGBoost, Neural Networks)
- [ ] Include weather API integration
- [ ] Add crop price predictions
- [ ] Implement user authentication
- [ ] Create mobile application
- [ ] Add multilingual support
- [ ] Include soil test interpretation
- [ ] Add fertilizer recommendations

## 📞 Support

For issues or questions:
1. Check the troubleshooting section
2. Review the code comments
3. Verify all files are in correct locations
4. Ensure all dependencies are installed

---

**Happy Farming! 🌱**