# 🛡️ Cybersecurity Threats Dataset Analysis

This Python script provides a quick and informative overview of the `Global_Cybersecurity_Threats_2015-2024.csv` dataset using the powerful `pandas` library.


## 📁 Dataset Overview

The dataset comprises 3,000 documented cybersecurity incidents worldwide, spanning from 2015 to 2024. Each entry includes details such as:

* **Country**
* **Year**
* **Attack Type**
* **Target Industry**
* **Financial Loss** (in Million USD)
* **Number of Affected Users**
* **Attack Source**
* **Vulnerability Type**
* **Defense Mechanism Used**
* **Incident Resolution Time** (in hours)

## 🧪 Script Features

This script performs a foundational exploration of the dataset through:

1. **Data Loading**: Reads the CSV into a pandas DataFrame.
2. **Structural Overview**: Displays data types and memory usage via `info()`.
3. **Initial Glimpse**: Outputs the first five records with `head()`.
4. **Missing Values Check**: Highlights any null entries using `isnull().sum()`.
5. **Statistical Summary**: Generates descriptive stats using `describe()`.

## 🗞 How to Run

1. Ensure the CSV file (`Global_Cybersecurity_Threats_2015-2024.csv`) is located in the same folder as the script.
2. Execute the script from your terminal:

```bash
python main.py
```

## 🧠 Requirements

* Python 3.x
* pandas library

If `pandas` isn't already installed, you can add it via pip:

```bash
pip install pandas
```

## 📊 Sample Output

The script will print:

* Dataset information (column names, data types, and memory usage)
* A preview of the first few rows
* A summary of missing values per column
* Descriptive statistics (mean, min, max, standard deviation, etc.)

