# Loan Approval Prediction System

## Introduction
The objective was to develop a model to predict the loan outcomes based on available user attributes and their GPS fixes. The data provided consisted of three datasets: `loan_outcomes`, `user_attributes`, and `user_gps_fixes`.

## Approach

### 1. Data Exploration
Initially loaded the datasets and conducted a preliminary exploration. This step helped identify potential missing values, anomalies, and patterns in the data.

### 2. Data Pre-processing 
- The loan outcome was converted to a numerical format for model training.
- Joined the user attributes and loan outcomes datasets on the 'user_id' column to combine information.
- Handled any missing or NaN values in the datasets.

### 3. Visualization
Employed multiple plots to understand the distribution, correlation, and relationship between variables and the loan outcome.

### 4. Modeling
- Employed Logistic Regression as the primary prediction model.
- Split the data into training and test sets.
- Trained the model on the training set and evaluated its performance on the test set.

### 5. API Development 
An API was developed to fetch data based on user_id and return predictions. If raw data is provided, it predicts directly, otherwise, it fetches the data from the database.

## Findings
1. The `loan_outcomes` dataset had an almost balanced number of defaults and repaid loans.
2. Age and cash income had different distributions, but clear patterns in relation to loan outcomes were not readily apparent in the exploratory analysis.
3. Model achieved an accuracy of 52.5% on the test set, indicating room for improvement.

## Next Steps with a Larger Dataset

1. **Enhanced Feature Engineering**: With more data, we could potentially find patterns from the user's geographic movements (e.g., frequent visitations to certain establishments might correlate with financial stability).

2. **Model Improvement**: Experiment with more advanced models like Random Forest, Gradient Boosting Machines, and Neural Networks.

3. **Hyperparameter Tuning**: Conduct an extensive hyperparameter search to optimize the model's performance.

4. **Ensemble Techniques**: Combine predictions from multiple models to achieve better accuracy.

5. **Anomaly Detection**: Implement anomaly detection to find any unusual patterns or potential fraud cases.

6. **Feedback Loop**: As users continue to take loans and either repay or default, continuously retrain the model to keep it up-to-date.


## Using the Loan Approval Prediction API with Postman

Postman provides a user-friendly interface to send requests to APIs. Here's a step-by-step guide to using the Loan Approval Prediction API via Postman:

### Prerequisites:

- Install [Postman](https://www.getpostman.com/downloads/).
  
### Steps:

1. **Open Postman**: Launch the application after installation.

2. **Create a New Request**:
    - Click on the '+' tab or 'Create a request'.
    - Select the HTTP method. For our API, we will use `POST`.

3. **Enter the API URL**: 
    - Copy and paste the API endpoint URL into the request URL field:
    ```bash
    http://127.0.0.1:5000/predict
    ```

3. **Add JSON Body**:
    - Click on the 'Body' tab.
    - Select 'raw' and choose 'JSON' from the dropdown.
    - Depending on the type of prediction:
      - For prediction using `user_id`: 
        ```json
        {
          "user_id": 2
        }
        ```
      - For prediction using raw data:
        ```json
        {
          "age": 25,
          "cash_incoming_30days": 1000
        }
        ```

4. **Send the Request**: 
    - Click the 'Send' button.
    - Postman will display the API's response at the bottom.

7. **Review the Response**:
    - You should see a prediction result in the response body. It will indicate whether the loan should be approved or not based on the provided data.

8. **Troubleshooting**:
    - If there's an error, check the response status and message for hints.
    - Ensure that the API endpoint URL and headers are correctly set.
    - Make sure your internet connection is stable.
