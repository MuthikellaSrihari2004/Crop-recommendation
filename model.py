import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import joblib
import os

def create_directories():
    """Create necessary directories if they don't exist"""
    os.makedirs('models', exist_ok=True)
    os.makedirs('data', exist_ok=True)

def load_and_prepare_data(filepath='data/Crop_recommendation.csv'):
    """Load and prepare the dataset"""
    print("Loading dataset...")
    df = pd.read_csv(filepath)
    
    print(f"Dataset shape: {df.shape}")
    print(f"\nDataset info:")
    print(df.info())
    print(f"\nFirst few rows:")
    print(df.head())
    print(f"\nCrop distribution:")
    print(df['label'].value_counts())
    
    return df

def preprocess_data(df):
    """Preprocess the data: separate features and target, encode labels"""
    print("\nPreprocessing data...")
    
    # Separate features and target
    X = df.drop('label', axis=1)
    y = df['label']
    
    # Encode target labels
    label_encoder = LabelEncoder()
    y_encoded = label_encoder.fit_transform(y)
    
    print(f"Features shape: {X.shape}")
    print(f"Target shape: {y_encoded.shape}")
    print(f"Classes: {label_encoder.classes_}")
    
    return X, y_encoded, label_encoder

def split_data(X, y, test_size=0.2, random_state=42):
    """Split data into training and testing sets"""
    print("\nSplitting data...")
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state, stratify=y
    )
    
    print(f"Training set size: {X_train.shape[0]}")
    print(f"Testing set size: {X_test.shape[0]}")
    
    return X_train, X_test, y_train, y_test

def scale_features(X_train, X_test):
    """Scale features using StandardScaler"""
    print("\nScaling features...")
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    return X_train_scaled, X_test_scaled, scaler

def train_model(X_train, y_train):
    """Train Random Forest Classifier"""
    print("\nTraining Random Forest model...")
    model = RandomForestClassifier(
        n_estimators=100,
        max_depth=20,
        min_samples_split=5,
        min_samples_leaf=2,
        random_state=42,
        n_jobs=-1
    )
    
    model.fit(X_train, y_train)
    print("Model training completed!")
    
    return model

def evaluate_model(model, X_test, y_test, label_encoder):
    """Evaluate model performance"""
    print("\nEvaluating model...")
    y_pred = model.predict(X_test)
    
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Accuracy: {accuracy * 100:.2f}%")
    
    print("\nClassification Report:")
    print(classification_report(y_test, y_pred, 
                                target_names=label_encoder.classes_))
    
    return accuracy

def save_models(model, scaler, label_encoder):
    """Save trained models and preprocessors"""
    print("\nSaving models...")
    joblib.dump(model, 'models/crop_model.pkl')
    joblib.dump(scaler, 'models/scaler.pkl')
    joblib.dump(label_encoder, 'models/label_encoder.pkl')
    print("Models saved successfully!")

def get_feature_importance(model, feature_names):
    """Display feature importance"""
    print("\nFeature Importance:")
    importance = pd.DataFrame({
        'feature': feature_names,
        'importance': model.feature_importances_
    }).sort_values('importance', ascending=False)
    print(importance)

def main():
    """Main training pipeline"""
    try:
        # Create directories
        create_directories()
        
        # Load data
        df = load_and_prepare_data()
        
        # Preprocess
        X, y, label_encoder = preprocess_data(df)
        
        # Split data
        X_train, X_test, y_train, y_test = split_data(X, y)
        
        # Scale features
        X_train_scaled, X_test_scaled, scaler = scale_features(X_train, X_test)
        
        # Train model
        model = train_model(X_train_scaled, y_train)
        
        # Evaluate
        accuracy = evaluate_model(model, X_test_scaled, y_test, label_encoder)
        
        # Feature importance
        get_feature_importance(model, X.columns)
        
        # Save models
        save_models(model, scaler, label_encoder)
        
        print("\n" + "="*50)
        print(f"Training completed successfully!")
        print(f"Final Accuracy: {accuracy * 100:.2f}%")
        print("="*50)
        
    except FileNotFoundError:
        print("Error: Dataset file not found!")
        print("Please place 'Crop_recommendation.csv' in the 'data' folder")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()