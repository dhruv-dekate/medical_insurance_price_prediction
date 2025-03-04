# Insurance Premium Prediction

## Overview
This is a **Streamlit web application** that predicts **medical insurance premiums** based on user inputs such as age, BMI, smoking status, and region. The model used for prediction is a **Random Forest Regressor** trained on a dataset with **One-Hot Encoded categorical features**.

## Features
- User-friendly web interface built with **Streamlit**.
- Predicts insurance premiums based on various input factors.
- Uses **One-Hot Encoding** to handle categorical features.
- Pre-trained **Random Forest Regression model** (`randomforest_reg.pkl`).

## Requirements
Make sure you have the following dependencies installed:

```bash
pip install streamlit pandas numpy scikit-learn
```

## Installation & Setup
1. Clone this repository:
   ```bash
   git clone https://github.com/your-repo/insurance-premium-prediction.git
   cd insurance-premium-prediction
   ```

2. Ensure you have the required dataset and model file:
   - `randomforest_reg.pkl` (Pre-trained model)
   - `medical_insurance_updated_dataset.csv` (Optional for reference)

3. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

## Usage
1. Open the app in your browser (Streamlit will automatically launch it).
2. Enter the required details:
   - **Age** (18-100)
   - **Sex** (Male/Female)
   - **BMI** (Body Mass Index)
   - **Children** (Number of children covered under insurance)
   - **Smoker** (Yes/No)
   - **Region** (Northeast, Northwest, Southeast, Southwest)
3. Click **Predict Premium** to get the estimated cost.

## Model Details
- **Algorithm Used:** Random Forest Regression
- **Feature Engineering:** One-Hot Encoding for categorical variables
- **Dataset Used:** Medical Insurance dataset

## Example Prediction
Input:
```
Age: 30
Sex: Male
BMI: 25.0
Children: 0
Smoker: Yes
Region: Southeast
```
Output:
```
Estimated Insurance Premium: $16,000.75
```

---
Made with ❤️ by [DHRUV DEKATE]