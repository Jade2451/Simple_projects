import requests

def get_dad_joke():
    """
    Fetches a random dad joke from the icanhazdadjoke.com API.
    """
    print("🤣 Dad Joke Generator 🤣")
    
    api_url = "https://icanhazdadjoke.com/"
    
    # --- The API requires a specific 'Accept' header to return JSON ---
    headers = {
        "Accept": "application/json",
        "User-Agent": "My Python Joke App (github.com/your-username)"
    }
    
    try:
        print("Fetching a high-quality dad joke...")
        response = requests.get(api_url, headers=headers)
        response.raise_for_status() # Check for request errors
        
        data = response.json()
        joke = data.get('joke')

        if joke:
            print("\n" + "="*70)
            print(joke)
            print("="*70 + "\n")
        else:
            print("Could not retrieve a joke. The API format may have changed.")

    except requests.exceptions.RequestException as e:
        print(f"\n❌ Error: Could not connect to the joke API.")
        print(f"   Details: {e}")

# --- Main execution block ---
if __name__ == "__main__":
    get_dad_joke()
