# gse-project-2

# CSV-python-project-2
This README file is designed to accompany your Dataset Management and Basic Analysis System project. It provides a professional overview of your code, its features, and how to run it.
# Dataset Management and Basic Analysis System
## Project Overview
This project is a Python-based tool designed to automate the loading, processing, and statistical analysis of numerical and categorical datasets. Built using Object-Oriented Programming (OOP) principles, the system handles data ingestion, error validation, and generates a detailed performance report.
The system is particularly useful for analyzing academic records (student marks) or sales figures to determine performance levels based on customizable thresholds.

## Features
**Robust File Handling: Reads from text and CSV formats with built-in error handling for missing files, empty files, or corrupted (non-numeric) data.
**Statistical Engine: Custom-built functions to calculate Total, Average, Minimum, and Maximumvalues using manual loop traversal and arithmetic operators.
**Categorical Analysis: Uses Python *Sets* to extract and count unique categories from a dataset, ensuring no duplicate entries are counted.
**Performance Tracking: Automatically evaluates the dataset average against a set threshold to label performance as "High Performance" or "Needs Improvement.
**Automated Reporting: Generates a formatted `report.txt` file containing the final calculated statistics and unique category counts.

## Technical Implementation
The project demonstrates core Python proficiencies
1. OOP (Object-Oriented Programming): Encapsulated logic within the `DataSet` class
2. Error Handling: Implementation of `try...except` blocks for data validation and file safety.
3. Data Structures: Advanced use of `lists` for data storage, `dictionaries` for statistics, and `sets` for unique values
4. Control Flow: Sophisticated `while` loops, `for` loops, and `match-case` statements for menu navigation
   
## File Structure
* `gse.py`: The main Python script containing the `DataSet` class and logic.
* `Create_test_data.py`: A utility script to generate sample `marks.txt` and `courses.txt` files for testing.
* `sample_data.csv`: A sample input file containing numerical data.
* `sample_categories.txt`: A sample input file containing categorical data.
* `report.txt`: The output report generated after running the analysis.

##  How to Run
1. Clone the Repository
```bash
git clone https://github.com/yourusername/gse301-python-project.git
```


2. Generate Test Data (Optional):
```bash
python Create_test_data.py
```
3. Execute the Analysis:
```bash
python gse.py
```
## Example Output
```text
--- Analysis Results ---
Total: 350.00
Average: 70.00
Minimum: 40.00
Maximum: 95.00
Total Unique Categories: 3
Status: High Performance
```


