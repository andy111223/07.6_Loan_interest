import numpy as np
import numpy_financial as npf
import matplotlib.pyplot as plt

def compare_interest_variants(pv, rate, years, freq=12):
    """
    Compare the total interest paid between equal payments and decreasing payments for a given loan.

    Parameters:
    pv (float): Present value or principal of the loan.
    rate (float): Annual interest rate (as a decimal).
    years (int): Number of years for the loan.
    freq (int, optional): Number of payment periods per year (default is 12).

    Returns:
    None
    """
    # Conversion of yearly rate to monthly rate
    rate /= freq
    nper = years * freq  # Number of periods

    periods = np.arange(1, nper + 1, dtype=int)
    # print(f"Periods:\n {periods}")

    # Equal payments
    interest_equal = -np.around(npf.ipmt(rate, periods, nper, pv), 2)
    # print(f"interest_equal:\n {interest_equal}")

    # Decreasing payments
    np.set_printoptions(suppress=True)

    principal_decreasing = np.around(np.zeros(nper) + (pv / nper), 2)
    # print(f"principal_decreasing:\n {principal_decreasing}")

    balance = np.zeros(nper) + pv
    # print(f"balance:\n {balance}")

    balance_close = np.around(balance - np.cumsum(principal_decreasing), 2)
    # print(f"balance_close:\n {balance_close}")

    balance_open = balance_close + principal_decreasing
    # print(f"balance_open:\n {balance_open}")

    interest_decreasing = np.around(balance_open * rate, 2)
    # print(f"interest_decreasing:\n {interest_decreasing}")

    # Comparison of interest paid in both variants
    print("Total interest in 'equal payments' variant: " + str("{:.2f}".format(interest_equal.sum())))
    print("Total interest in 'decreasing payments' variant: " + str("{:.2f}".format(interest_decreasing.sum())))
    print("Difference between the two variants: " + str("{:.2f}".format(interest_equal.sum() - interest_decreasing.sum())))

    # Plotting the cumulative interest comparison
    plt.plot(interest_equal.cumsum(), label='equal payments')
    plt.plot(interest_decreasing.cumsum(), label='decreasing payments')
    plt.legend()
    plt.xlabel('Number of periods')
    plt.ylabel('Cumulative interest')

    # Display the plot
    plt.title('Cumulative Interest Comparison')
    plt.show()

# Example usage
compare_interest_variants(pv=200000, rate=0.0675, years=30)