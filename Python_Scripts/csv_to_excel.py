import pandas as pd
import os

csv_file_name=input("Enter the name of the CSV file to convert to Excel: ")

if not csv_file_name.endswith(".csv"):
  csv_file_name = '.'.join([csv_file_name, "csv"])
else:
  pass


# Read the CSV file

# Convert the DataFrame to an Excel spreadsheet
try: 
    print("Locating " + csv_file_name)
    df = pd.read_csv(os.path.join("./files", csv_file_name))
    print("Converting " + csv_file_name)
    df.to_excel("./files/converted.xlsx")
    print("Successfully converted " + csv_file_name)

except:
    print("Error converting the file, try again!")
