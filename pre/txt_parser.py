with open("pre/parsed_text.txt", "r") as file:
    text = file.read()
    
print(text)

import re

# Regex pattern
pattern = r'\d+\.?\s*(.*)'

# Find all matches
matches = re.findall(pattern, text)

# Print the results
print(matches)

print(len(matches))

import csv

# Write the list of words to a CSV file
with open('words.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    # Write each word on a new row
    for word in matches:
        writer.writerow([word])