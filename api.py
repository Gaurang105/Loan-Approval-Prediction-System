from flask import Flask, request, jsonify
import joblib
import psycopg2

app = Flask(__name__)
model = joblib.load("model.pkl")


# Database configurations
DB_NAME = "branchdsprojectgps"
DB_USER = "datascientist"
DB_PASSWORD = "47eyYBLT0laW5j9U24Uuy8gLcrN"
DB_HOST = "branchhomeworkdb.ccc0r2wfuew7.us-east-1.rds.amazonaws.com"
DB_PORT = "5432"

def get_db_connection():
    return psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST, port=DB_PORT)

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()

        if "age" in data and "cash_incoming_30days" in data:
            age = data["age"]
            cash_incoming_30days = data["cash_incoming_30days"]

        elif "user_id" in data:
            user_id = data["user_id"]
            
            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute(f"SELECT age, cash_incoming_30days FROM user_attributes WHERE user_id = {user_id}")
            user_data = cursor.fetchone()

            if not user_data:
                return jsonify({"error": "User data not found"}), 404

            age, cash_incoming_30days = user_data

            cursor.close()
            conn.close()
        else:
            return jsonify({"error": "Either user_id or user attributes must be provided"}), 400

        # Prediction using the loaded model
        prediction = model.predict([[age, cash_incoming_30days]])[0]

        # Converting prediction to string
        prediction_str = "repaid" if prediction == 1 else "defaulted"

        return jsonify({"prediction": prediction_str})

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)
