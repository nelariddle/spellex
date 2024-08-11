import requests

# Replace with your own API key
api_key = "1e8c5165-5cb2-4492-9e34-37c480bb78ae"
word = "bacteria"
url = f"https://www.dictionaryapi.com/api/v3/references/collegiate/json/{word}?key={api_key}"

response = requests.get(url)
data = response.json()

print(data)
# Extract the first definition if available
if data:
    if isinstance(data[0], dict) and 'shortdef' in data[0]:
        definition = data[0]['shortdef'][0]
        print(f"Definition of '{word}': {definition}")
    else:
        print(f"No definition found for '{word}'.")
else:
    print("Word not found in the dictionary.")
