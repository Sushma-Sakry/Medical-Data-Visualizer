# Medical Data Visualizer

This project is part of the Data Analysis with Python certification from freeCodeCamp.

The project analyzes medical examination data using Python libraries such as Pandas, Matplotlib, Seaborn, and NumPy. The dataset contains information related to patient body measurements, blood test results, lifestyle habits, and cardiovascular disease.

## Project Objectives

The main objectives of this project are:

- Import and analyze medical examination data
- Calculate Body Mass Index (BMI)
- Add an overweight feature based on BMI
- Normalize cholesterol and glucose values
- Clean incorrect or unrealistic data
- Create categorical visualizations
- Generate a correlation heatmap for medical indicators

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Google Colab

## Files Included

- `medical_data_visualizer.py` → Main project code
- `medical_examination.csv` → Dataset used for analysis
- `catplot.png` → Categorical plot visualization
- `heatmap.png` → Correlation heatmap visualization

## Features Implemented

### 1. Overweight Calculation

BMI was calculated using:

BMI = weight / (height in meters)^2

Patients with BMI > 25 were marked as overweight.

### 2. Data Normalization

Cholesterol and glucose values were normalized:
- 0 → healthy
- 1 → unhealthy

### 3. Categorical Plot

A categorical plot was created to compare:
- cholesterol
- glucose
- smoking
- alcohol intake
- physical activity
- overweight condition

for patients with and without cardiovascular disease.

### 4. Heatmap

A correlation heatmap was generated after cleaning invalid data such as:
- incorrect blood pressure values
- extreme height values
- extreme weight values

## Dataset Information

The dataset contains medical examination records of 70,000 patients with features including:
- age
- gender
- height
- weight
- blood pressure
- cholesterol
- glucose
- smoking habits
- alcohol consumption
- physical activity
- cardiovascular disease status
