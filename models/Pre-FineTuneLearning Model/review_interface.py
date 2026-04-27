from flask import Flask, render_template, request, redirect, url_for
import os
import random
import csv
from datetime import datetime

app = Flask(__name__)

# Define unified classification criteria (12 categories)
classification_criteria = [
    "Telltale Icons & Indicators",
    "System Architecture Diagrams",
    "Configuration Tables & Data",
    "State Matrix & Transitions",
    "Workflow & Process Diagrams",
    "Timing Diagrams & Sequences",
    "Data Flow Diagrams",
    "UI Design & Components",
    "HMI Display Layouts",
    "Wireframes & Mockups",
    "Test Cases & Validation",
    "Technical Specifications & Descriptions"
]

# Directory containing images
image_directory = "SRS FPI export/SRS_Instrument Cluster"

# List to store all image paths
image_paths = []

# Function to get all image paths
def get_image_paths():
    global image_paths
    image_paths = []
    for root, dirs, files in os.walk(image_directory):
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
                image_paths.append(os.path.relpath(os.path.join(root, file), image_directory))

# Route to display a random image
@app.route('/')
def display_image():
    get_image_paths()
    random_image = random.choice(image_paths)
    
    # Read automated classification
    automated_classification = None
    with open('image_classifications.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == random_image:
                automated_classification = row[2]
    
    return render_template('review_template.html', image_path=random_image, criteria=classification_criteria, automated_classification=automated_classification)

# Route to handle form submission
@app.route('/submit', methods=['POST'])
def submit_classification():
    image_path = request.form['image_path']
    user_classifications = request.form.getlist('classification')
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    with open('user_classifications.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([image_path, ', '.join(user_classifications), timestamp])
    
    return redirect(url_for('display_image'))

import sys

if __name__ == '__main__':
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 5001
    app.run(debug=True, port=port)
