import re

import PyPDF2

pdf_path = "/Users/mac/Desktop/bank.pdf"


def extract_text_from_pdf(pdf_path):
    text = ""
    with open(pdf_path, "rb") as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            text += page.extract_text()
    return text


def extract_names_and_amounts(text):
    transactions = []
    lines = text.split('\n')
    print(lines);
    
    for line in lines:
        match = re.search(r'([A-Za-z\s]+)\s+(\d+\.\d+)', line)
        if match:
            name = match.group(1).strip()
            amount = float(match.group(2))
            transactions.append((name, amount))
    return transactions


pdf_text = extract_text_from_pdf(pdf_path)
transactions = extract_names_and_amounts(pdf_text)

name_amount_mapping = {}
total_amount = 0

for name, amount in transactions:
    total_amount += amount
    if name in name_amount_mapping:
        name_amount_mapping[name] += amount
    else:
        name_amount_mapping[name] = amount

# Print the total amount and name-amount mapping
print("Total Amount:", total_amount)
for name, amount in name_amount_mapping.items():
    print(f"{name}: {amount}")
