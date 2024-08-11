import PyPDF2

# Open the PDF file
with open('spellelemwordlist.pdf', 'rb') as file:
    # Create a PDF reader object
    reader = PyPDF2.PdfReader(file)

    # Iterate through each page and extract text
    text = ""
    for page_num in range(len(reader.pages)):
        page = reader.pages[page_num]
        text += page.extract_text()

    # Print the extracted text
    print(text)
    
with open("pre/parsed_text.txt", "w") as file:
    file.write(text)