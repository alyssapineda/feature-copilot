from utils.credentials import Credentials
import csv
import pandas as pd

#Change path
PATH = Credentials.get_csv_path(filename="fred_financial_labor_performance.csv")

def read_csv(csv_file):
  columns = []
  #TO-DO: further pre processing to deal with weird gaps in comments column?
  with open(csv_file, 'r', newline='') as file:
      reader = csv.DictReader(file)
      for row in reader:
          columns.append(row)
  return columns

def generate_md_doc(number, name, header, description, output_file, columns):
  with open(output_file, 'w') as md_doc:
    md_doc.write(f"**Table {table_number}: {table_name}** ({table_header} information)\n\nThis table contains information about {table_description.lower()} and their attributes\n")
    md_doc.write("\n")

    for column in columns:
      column_name = column['COLUMN_NAME']
      data_type = column['DATA_TYPE']
      numeric_precision = column['NUMERIC_PRECISION']
      numeric_scale = column['NUMERIC_SCALE']
      character_max_length = column['CHARACTER_MAXIMUM_LENGTH']
      comment = column['COMMENT'] 
      is_nullable = column['IS_NULLABLE']

      md_doc.write(f"- {column_name}: ")

      if data_type == 'NUMBER':
        md_doc.write(f"Number ({numeric_precision}, {numeric_scale})")
      elif data_type == 'TEXT':
        md_doc.write(f"Varchar ({character_max_length})")
      else:
        md_doc.write(f"Date")

      md_doc.write(f" - {comment} (Nullable: {is_nullable})\n")
      md_doc.write("\n")

#Change table number, table name, table header, table description, output md path
table_number = "2"
table_name = "banking_analytics_bundle.banking_insights.Financial Labout Performance".upper()
table_header = "Economic and Financial Labor Performance Data"
table_description = "related to economic and financial labor performance, including employment, industrial production, and labor force participation"
output_md_path = '/Users/alyssapineda/feature-copilot/feature-copilot/docs/fred_financial_labor_performance.md'
columns = read_csv(PATH)
generate_md_doc(table_number, table_name, table_header, table_description, output_md_path, columns)