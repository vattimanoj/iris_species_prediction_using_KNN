#  Iris Flower Classification using KNN

## 📌 Project Overview

This project is a **Machine Learning web application** that predicts the species of an Iris flower using the **K-Nearest Neighbors (KNN)** classification algorithm.

The model is trained using the Iris dataset and uses four flower measurements:

* Sepal Length
* Sepal Width
* Petal Length
* Petal Width

The trained model is saved using **Pickle** and integrated with a **Flask web application** for making predictions.

## 🎯 Objective

The main objective of this project is to build a machine learning classification model that can identify an Iris flower species based on its physical measurements.

The model classifies flowers into:

* 🌱 Iris Setosa
* 🌸 Iris Versicolor
* 🌺 Iris Virginica

## 🛠️ Technologies Used

* **Python**
* **Pandas**
* **Scikit-learn**
* **K-Nearest Neighbors (KNN)**
* **Flask**
* **Pickle**
* **HTML/CSS**
* **Iris Dataset**

## 📂 Project Structure

```text
Iris-Flower-Classification/
│
├── app.py
├── model.py
├── Iris.csv
├── model.pkl
├── templates/
│   └── index.html
└── README.md
```

## ⚙️ Machine Learning Workflow

```text
Iris Dataset
     ↓
Data Preprocessing
     ↓
Remove ID Column
     ↓
Encode Species
     ↓
Train/Test Split
     ↓
KNN Model
     ↓
Model Evaluation
     ↓
Save Model using Pickle
     ↓
Flask Web Application
     ↓
Flower Species Prediction
```

## 🧠 Model Development

The dataset is loaded using Pandas. The `Id` column is removed, and the categorical species values are converted into numerical labels. The first four columns are used as input features and `Species` is used as the target variable.

The dataset is divided into training and testing sets using an **80:20 split** with `random_state=42`.

The project uses `KNeighborsClassifier` for classification and evaluates the model using:

* Accuracy Score
* Confusion Matrix
* Classification Report

## 💾 Model Saving

After training, the KNN model is saved as:

```text
model.pkl
```

using Python's `pickle` module.

## 🌐 Flask Web Application

The Flask application loads the trained model and provides two main routes:

```text
/       → Home page
/predict → Prediction
```

The prediction route receives the four flower measurements from the web form and passes them to the trained model.

The predicted numerical class is converted into the corresponding Iris species name:

```text
0 → iris-setosa
1 → iris-versicolor
2 → iris-verginica
```

## 🚀 How to Run the Project

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd Iris-Flower-Classification
```

### 2. Install required libraries

```bash
pip install pandas numpy scikit-learn flask
```

### 3. Train the model

```bash
python model.py
```

This trains the KNN model and creates:

```text
model.pkl
```

### 4. Start the Flask application

```bash
python app.py
```

### 5. Open the application

Open your browser and visit:

```text
http://127.0.0.1:5000/
```

## 🔮 Example Prediction

Input:

```text
Sepal Length: 7.7
Sepal Width: 3.6
Petal Length: 6.0
Petal Width: 2.0
```

The trained model predicts the corresponding Iris species.

## 📊 Model Evaluation

The project evaluates both training and testing performance using:

* Confusion Matrix
* Accuracy
* Classification Report

The evaluation code is implemented in the `train()` and `test()` methods.

## 📌 Future Improvements

* Improve the web interface with a modern UI
* Add data visualization
* Compare KNN with other classification algorithms
* Add model performance graphs
* Deploy the application online
* Add input validation
* Improve prediction error handling

## 👨‍💻 Author

**Manoj Vatti**

B.Tech – Computer Science Engineering

## ⭐ Conclusion

This project demonstrates the complete workflow of a machine learning application, from **data preprocessing and model training to model deployment using Flask**.

If you find this project useful, consider giving the repository a ⭐.
## 🌐 Live Deployment

The Iris Flower Classification application is deployed online using **Render**.

🔗 **Live Demo:**
https://iris-species-prediction-using-knn.onrender.com
