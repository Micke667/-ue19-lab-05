import requests

def get_joke():
    """Fetch a random joke from JokesAPI."""
    url = "https://v2.jokeapi.dev/joke/Any?type=single"
    try:
        response = requests.get(url)
        response.raise_for_status()
        joke_data = response.json()
        if 'joke' in joke_data:
            return joke_data['joke']
        else:
            return "No joke found."
    except requests.exceptions.RequestException as e:
        return f"An error occurred: {e}"

if __name__ == "__main__":
    print("Fetching a random joke...")
    joke = get_joke()
    print(f"Here's a joke for you: {joke}")
