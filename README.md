# 🌾 Crop Yield Prediction System
This project is a **Machine Learning web application** that predicts crop yield based on environmental and agricultural parameters. The application is built using **Python** and **Streamlit**, providing an interactive interface for users.

---

# 🚀 Features
- Predict crop yield using machine learning.
- User-friendly web interface.
- Input agricultural parameters such as:
  - Year
  - Average Rainfall
  - Pesticides Usage
  - Average Temperature
  - Area (Country)
  - Crop Type
- Instant yield prediction.

---

# 🛠 Technologies Used
- Python
- Streamlit
- Pandas
- NumPy
- Scikit-learn

---

# 📊 Machine Learning Model
The model was trained using agricultural datasets and utilizes a **Decision Tree Regressor** to predict crop yield.

---

# 📂 Project Structure
CropYield/
│
├── app.py # Streamlit application file
├── dt.pkl # Trained Decision Tree model
├── preprocessor.pkl # Preprocessing pipeline
├── crop.ipynb # Jupyter notebook for model training
└── yield_df.csv # Dataset used for training

# Install Dependencies :
pip install pandas numpy streamlit scikit-learn

# 🌐 Deployment 
The application can be deployed easily using Streamlit Community Cloud by connecting the GitHub repository.
