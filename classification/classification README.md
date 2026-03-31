# 🧠 Breast Cancer Prediction using Machine Learning

## 📌 Project Overview
This project predicts whether a tumor is **malignant** or **benign** using multiple machine learning classification algorithms.

The dataset is taken from Scikit-learn’s built-in Breast Cancer dataset.

---

## 📂 Dataset Information
- Source: sklearn.datasets.load_breast_cancer
- Features: 30 numerical features
- Target:
  - 0 → Malignant (Cancerous)
  - 1 → Benign (Non-cancerous)

---

## 🛠️ Technologies Used
- Python
- Pandas
- Scikit-learn

---

## ⚙️ Models Used & Accuracy

| Model                     | Accuracy |
|--------------------------|----------|
| AdaBoostClassifier       | **97%** ⭐ (Best Model) |
| GradientBoostingClassifier | 96% |
| DecisionTreeClassifier   | 95% |
| KNeighborsClassifier     | 94% |
| SVC                      | 90% |
| MultinomialNB            | 87% |

---

## 🚀 Features
- Multiple model comparison
- High accuracy classification
- Clean dataset handling using Pandas
- Beginner-friendly ML workflow

---

## 📈 Key Insight
👉 **AdaBoostClassifier performed best with 97% accuracy**, making it the most reliable model for this dataset.

---

## ▶️ How to Run

```bash
pip install pandas scikit-learn
python your_file_name.py