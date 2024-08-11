import requests
import csv

# Replace with your own API key
api_key = "1e8c5165-5cb2-4492-9e34-37c480bb78ae"
word = "autism"
url = f"https://www.dictionaryapi.com/api/v3/references/collegiate/json/{word}?key={api_key}"


input_file = "words.csv"
output_file = "definitions.csv"

# Open the input file (words.csv) and output file (definitions.csv)
with open(input_file, mode="r", encoding="utf-8") as infile, open(
    output_file, mode="w", newline="", encoding="utf-8"
) as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)

    # Write the header to the output file
    writer.writerow(["Word", "Definition"])

    # Iterate over each word in the input file
    for row in reader:
        word = row[0]
        url = f"https://www.dictionaryapi.com/api/v3/references/collegiate/json/{word}?key={api_key}"

        response = requests.get(url)
        data = response.json()

        # Extract the first definition if available
        # if data and isinstance(data[0], dict) and 'shortdef' in data[0]:
        #     definition = data[0]['shortdef'][0]
        # else:
        #     definition = "No definition found"

        try:
            definition = data[0]["shortdef"][0]
        except:
            definition = ""

        # Write the word and its definition to the output file

        print([word, definition])
        writer.writerow([word, definition])

print(f"Definitions have been written to {output_file}")
