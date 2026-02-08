import csv
import os

class NeuroLogger:
    def __init__(self, filename="data/neuro_data.csv"):
        self.filename = filename
        if not os.path.exists('data'): os.makedirs('data')
        
    def log(self, t, input_val, output_val):
        with open(self.filename, mode='a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([t, input_val, output_val])
