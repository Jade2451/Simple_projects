def get_positive_float(prompt):
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

def calculate_bmi():
    """
    Calculates BMI and provides a classification.
    """
    print("🧑‍⚕️ BMI (Body Mass Index) Calculator 🧑‍⚕️")
    
    # --- Get User Input ---
    # Formula uses kilograms and meters
    print("\nPlease enter your weight in kilograms (kg):")
    weight_kg = get_positive_float("> ")
    
    print("\nPlease enter your height in meters (m) (e.g., 1.75):")
    height_m = get_positive_float("> ")

    # --- Calculate BMI ---
    # Formula: weight (kg) / (height (m) ^ 2)
    bmi = weight_kg / (height_m ** 2)

    # --- Determine Classification ---
    if bmi < 18.5:
        classification = "Underweight"
    elif 18.5 <= bmi < 24.9:
        classification = "Normal weight"
    elif 25 <= bmi < 29.9:
        classification = "Overweight"
    else:
        classification = "Obesity"

    # --- Display Results ---
    print("\n" + "="*35)
    print("          Your Results")
    print("="*35)
    print(f"  Your BMI is: {bmi:.2f}")
    print(f"  Classification: {classification}")
    print("="*35)
    print("\nNote: BMI is a general guide and may not be")
    print("accurate for all body types (e.g., athletes).")

# --- Main execution block ---
if __name__ == "__main__":
    calculate_bmi()
