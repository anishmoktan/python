# import pdfplumber

# def convert_pdf_to_text(pdf_path):
#     text = ""
#     with pdfplumber.open(pdf_path) as pdf:
#         for page in pdf.pages:
#             text += page.extract_text()
#     return text

# # Replace 'input.pdf' with the path to your PDF file
# pdf_text = convert_pdf_to_text('Anish_Tamang_KuraLabs_Resume.pdf')
# print(pdf_text)

import pdfplumber

def convert_pdf_to_text(pdf_path, output_path):
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text()
    
    with open(output_path, 'w', encoding='utf-8') as output_file:
        output_file.write(text)

# Replace 'input.pdf' with the path to your PDF file
pdf_path = input("Enter the name of the pdf file: ")

# Replace 'output.txt' with the desired path for the output text file
output_path = input("Enter the desired extracted file name: ")

convert_pdf_to_text(pdf_path, output_path)
print("Text extracted and saved to", output_path)
