from flask import Flask, render_template, request, jsonify
import pandas as pd
import os
from glob import glob
import subprocess
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def display_data():
    # Get the latest CSV file
    latest_file = get_latest_csv_file()
    data = read_csv_data(latest_file)
    print(data) # Add this line to check data in console
    return render_template('display_data.html', data=data)

@app.route('/trigger_scraper', methods=['POST'])
def trigger_scraper():
    # Execute milikispace.py using subprocess
    process = subprocess.Popen(["python3", "milikispace.py"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()

    if stderr:
        return 'Error occurred'
    else:
        # Update milikispace.csv file using time stamp
        latest_file = get_latest_csv_file()
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(latest_file, 'a') as file:
            file.write(f"Last Updated: {now}\n")

        return 'Scraper executed successfully'

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
        #data = df.to_dict(orient='records')
        data = df['Column'].tolist()
        print(data) # Add this line to print data
        return data
    else:
        return []

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8000))
    app.run(host='0.0.0.0', port=port)
    # Use Gunicorn to run the flask app
    cmd = f"gunicorn -b 0.0.0.0:{port} manage:app"
    subprocess.Popen(cmd, shell=True)
    #app.run(host='0.0.0.0', port=8000)
    # If running locally
   #app.run(port=5000, debug=True)
