import pandas as pd
import numpy as np
import scipy.stats as stats
import logging
import matplotlib.pyplot as plt
import seaborn as sns

# Setup logging
logging.basicConfig(filename='data_log.log', level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')

def read_data(file_path):
    """Read data from a CSV file."""
    try:
        data = pd.read_csv(file_path)
        logging.info("Data read successfully from {}".format(file_path))
        return data
    except Exception as e:
        logging.error("Error reading data: {}".format(e))
        return None

def analyze_data(data):
    """Perform statistical analysis on the data."""
    # Example: Shapiro-Wilk Test for normality on the first column of the data
    sw_test = stats.shapiro(data.iloc[:, 0])
    logging.info("Shapiro-Wilk Test performed with p-value: {}".format(sw_test.pvalue))

    # Additional analysis can be added here

def visualize_data(data):
    """Visualize the data using a plot."""
    plt.figure(figsize=(8, 6))
    sns.boxplot(data=data)
    plt.title("Data Visualization")
    plt.show()
    logging.info("Data visualization generated.")

# Main process
file_path = 'your_data.csv'  # Replace with your CSV file path
data = read_data(file_path)

if data is not None:
    analyze_data(data)
    visualize_data(data)

