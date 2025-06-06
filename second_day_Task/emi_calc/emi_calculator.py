def get_user_input():
    """Get principal, annual interest rate, and tenure in months from user."""
    try:
        principal = float(input("Enter the loan amount (Principal): "))
        annual_rate = float(input("Enter the annual interest rate (in %): "))
        tenure_months = int(input("Enter the loan tenure (in months): "))
        return principal, annual_rate, tenure_months
    except ValueError:
        print("Invalid input! Please enter numeric values only.")
        return None, None, None

def compute_emi(principal, annual_rate, tenure_months):
    """Compute EMI using the standard formula."""
    monthly_rate = annual_rate / (12 * 100)
    if monthly_rate == 0:  
        emi = principal / tenure_months
    else:
        emi = (principal * monthly_rate * (1 + monthly_rate) ** tenure_months) / \
              ((1 + monthly_rate) ** tenure_months - 1)
    return emi

def display_emi_result(principal, annual_rate, tenure_months, emi):
    """Display the EMI and summary of loan details."""
    total_payment = emi * tenure_months
    total_interest = total_payment - principal

    print("\nEMI Calculation Result:")
    print(f"Loan Amount (Principal): ₹{principal:,.2f}")
    print(f"Annual Interest Rate: {annual_rate:.2f}%")
    print(f"Loan Tenure: {tenure_months} months")
    print(f"Monthly EMI: ₹{emi:,.2f}")
    print(f"Total Payment: ₹{total_payment:,.2f}")
    print(f"Total Interest Payable: ₹{total_interest:,.2f}")

def calculate_emi():
    """Main function to coordinate EMI calculation."""
    principal, annual_rate, tenure_months = get_user_input()
    if principal and annual_rate is not None and tenure_months:
        emi = compute_emi(principal, annual_rate, tenure_months)
        display_emi_result(principal, annual_rate, tenure_months, emi)

if __name__ == '__main__':
    calculate_emi()
