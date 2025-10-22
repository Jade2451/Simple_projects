import requests

def get_random_quote():
    """
    Fetches a random quote from the quotable.io API and displays it.
    """
    print("💬 Random Quote Generator 💬")
    api_url = "https://api.quotable.io/random"
    
    try:
        print("Fetching a random quote...")
        response = requests.get(api_url)
        response.raise_for_status() # Check for any request errors
        
        data = response.json()
        quote = data.get('content')
        author = data.get('author')

        if quote and author:
            print("\n" + "="*70)
            print(f" \"{quote}\"")
            print(f"   - {author}")
            print("="*70)
        else:
            print("Could not retrieve a quote from the API response.")

    except requests.exceptions.RequestException as e:
        print(f"\n❌ Error: Could not connect to the quote API. Please check your internet connection.")
        print(f"   Details: {e}")

# --- Main execution block ---
if __name__ == "__main__":
    get_random_quote()
