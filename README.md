# Loan Interest Comparison

The Loan Interest Comparison script is a Python function designed to compare the total interest paid between two different types of loan repayment plans: equal payments and decreasing payments.

## Features
- Equal Payments vs. Decreasing Payments: calculates and compares the total interest for loans repaid with equal monthly payments and decreasing payments.
- Detailed Interest Breakdown: calculates the cumulative interest for each variant over time.
- Data Visualization: plots the cumulative interest over time for easy visual comparison.

## Installation
1. Clone this repository to your local machine:  
   ```git clone https://github.com/andy111223/07.6_Loan_interest.git```
2. Navigate to the project directory:  
   ```cd 07.6_Loan_interest```
3. Install the required dependencies (if not already installed):  
   ```pip install numpy numpy-financial matplotlib```
4. Run the script:  
   ```python3 main.py```

## Usage
- Import the compare_interest_variants function from the script to use it in your projects.
- Call the function with the following parameters:
    - pv: present value (loan principal amount).
    - rate: annual interest rate as a decimal (e.g., 0.0675 for 6.75%).
    - years: number of years for the loan.
    - freq: (optional) number of payment periods per year (default is 12).
The function will print the total interest for both variants and display a plot comparing the cumulative interest over the entire loan period.

## Requirements
- Python 3 (tested on Python 3.12)
- NumPy library
- NumPy-financial library
- Matplotlib library

