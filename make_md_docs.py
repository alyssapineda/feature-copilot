import csv
import json


def read_csv(csv_file):
  columns = []
  #TO-DO: further pre processing to deal with weird gaps in comments column?
  with open(csv_file, 'r', newline='') as file:
      reader = csv.DictReader(file)
      for row in reader:
          columns.append(row)
  return columns

def generate_md_doc(table_number, table_name, table_header, table_description, output_file, columns):
  with open(output_file, 'w') as md_doc:
    md_doc.write(f"**Table {table_number}: {table_name}** ({table_header})\n\n{table_description}\n")
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

def collect_table_info(csv_info):
  csv_path = csv_info['path']
  table_number = csv_info['table_number']
  table_name = csv_info['table_name']
  table_header = csv_info['table_header']
  table_description = csv_info['table_description']
  output_md_path= f"docs/{table_name}.md"
  
  columns = read_csv(csv_path)
  generate_md_doc(table_number, table_name, table_header, table_description, output_md_path, columns)



def main():
  #TO-DO: To scale, you move this csv_file_list as json?
  #If we have unlabelled company tables, how would we know what table header and descriptions to put?
  #Instead of saving csv files to csv folder, can connect to snowflake?

  with open('tables_info.json', 'r') as table_info:
    table_info_list = json.load(table_info)

    for tables in table_info_list:
      collect_table_info(tables)




if __name__ == "__main__":
  main()