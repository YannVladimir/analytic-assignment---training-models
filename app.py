{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "7b4575a2",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " * Serving Flask app '__main__'\n",
      " * Debug mode: on\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.\n",
      " * Running on http://127.0.0.1:5001\n",
      "Press CTRL+C to quit\n",
      " * Restarting with watchdog (windowsapi)\n"
     ]
    },
    {
     "ename": "SystemExit",
     "evalue": "1",
     "output_type": "error",
     "traceback": [
      "An exception has occurred, use %tb to see the full traceback.\n",
      "\u001b[1;31mSystemExit\u001b[0m\u001b[1;31m:\u001b[0m 1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\Yann\\anaconda3\\Lib\\site-packages\\IPython\\core\\interactiveshell.py:3513: UserWarning: To exit: use 'exit', 'quit', or Ctrl-D.\n",
      "  warn(\"To exit: use 'exit', 'quit', or Ctrl-D.\", stacklevel=1)\n"
     ]
    }
   ],
   "source": [
    "from flask import Flask, render_template, request, jsonify\n",
    "import pickle\n",
    "import pandas as pd\n",
    "\n",
    "app = Flask(__name__)\n",
    "\n",
    "# Load the final benchmark model\n",
    "with open('final_benchmark_model.pkl', 'rb') as model_file:\n",
    "    final_model = pickle.load(model_file)\n",
    "\n",
    "# Define a route for the home page\n",
    "@app.route('/')\n",
    "def home():\n",
    "    return render_template('index.html')\n",
    "\n",
    "# Define a route for receiving predictions\n",
    "@app.route('/predict', methods=['POST'])\n",
    "def predict():\n",
    "    # Get input data from the form\n",
    "    input_data = [float(request.form['PURCHASES']), float(request.form['PAYMENTS']), ...]  # Update with your feature names\n",
    "\n",
    "    # Convert input data to a DataFrame\n",
    "    input_df = pd.DataFrame([input_data], columns=['PURCHASES', 'PAYMENTS', ...])  # Update with your feature names\n",
    "\n",
    "    # Make predictions using the final model\n",
    "    prediction = final_model.predict(input_df)\n",
    "\n",
    "    # Return the prediction as a response\n",
    "    return render_template('result.html', prediction=prediction[0])\n",
    "\n",
    "# Run the Flask app\n",
    "if __name__ == '__main__':\n",
    "    app.run(debug=True, port=5001)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1568c02e",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
