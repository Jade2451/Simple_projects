def get_float_input(prompt):
    """Helper function to get valid positive float input."""
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Please enter a positive value.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a number.")

def calculate_simple_interest():
    """
    Calculates simple interest and total amount.
    """
    print("💰 Simple Interest Calculator 💰")
    
    # --- Get User Input ---
    principal = get_float_input("Enter the principal amount ($): ")
    rate = get_float_input("Enter the annual interest rate (%): ")
    time = get_float_input("Enter the time in years: ")

    # --- Calculate ---
    # Simple Interest formula: I = P * R * T
    interest = (principal * (rate / 100) * time)
    total_amount = principal + interest

    # --- Display Results ---
    print("\n" + "="*30)
    print("      Calculation Results")
    print("="*30)
    print(f"  Principal:   ${principal:,.2f}")
    print(f"  Interest:    ${interest:,.2f}")
    print("------------------------------")
    print(f"  Total Amount: ${total_amount:,.2f}")
    print("="*30)

# --- Main execution block ---
if __name__ == "__main__":
    calculate_simple_interest()
