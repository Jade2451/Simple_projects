def is_prime(n):
    """
    Checks if a number 'n' is prime.
    Returns True if prime, False otherwise.
    """
    if n <= 1:
        return False
    # 2 is the only even prime number
    if n == 2:
        return True
    # All other even numbers are not prime
    if n % 2 == 0:
        return False
    # Check odd divisors from 3 up to the square root of n
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False 
    #such a beautiful logic 
    # If no divisors were found, it's prime!
    return True

def main():
    """
    Main function to get user input and find primes in that range.
    """
    print("... Prime Number Finder ...")
    
    # --- Get Start Number ---
    while True:
        try:
            start = int(input("Enter the start number (e.g., 1): "))
            if start < 0:
                print("Please enter a non-negative number.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a whole number.")
            
    # --- Get End Number ---
    while True:
        try:
            end = int(input("Enter the end number (e.g., 100): "))
            if end <= start:
                print(f"The end number must be greater than {start}.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a whole number.")

    print(f"\nFinding prime numbers between {start} and {end}...")
    
    primes_found = []
    # Loop from the start number to the end number (inclusive)
    for num in range(start, end + 1):
        if is_prime(num):
            primes_found.append(num)
            
    # --- Display the Results ---
    if not primes_found:
        print(f"No prime numbers were found between {start} and {end}.")
    else:
        print("\n--- Primes Found ---")
        # Print the list as a comma-separated string
        print(", ".join(map(str, primes_found)))
        print(f"\nTotal: {len(primes_found)} primes found.")

# --- Main execution block ---
if __name__ == "__main__":
    main()
