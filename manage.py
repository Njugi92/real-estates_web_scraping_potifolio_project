from flask import Flask, render_template
import pandas as pd
import os
from glob import glob

app = Flask(__name__)

@app.route('/')
def display_data():
    # Get the latest CSV file
    latest_file = get_latest_csv_file()
    data = read_csv_data(latest_file)
    return render_template('display_data.html', data=data)

def get_latest_csv_file():
    # Get a list of all CSV files in the csv_data folder
    csv_files = glob('csv_data/*.csv')
    # Sort the files by modification time to get the latest one
    latest_file = max(csv_files, key=os.path.getmtime) if csv_files else None
    return latest_file

def read_csv_data(filename):
    # Read data from the CSV file
    if filename:
        df = pd.read_csv(filename)
        return df.to_dict(orient='records')
    else:
        return []

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
    # If running locally
   #app.run(port=5000, debug=True) 
