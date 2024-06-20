import csv, json, os

#function to get table info from CSV files from csv folder
def get_table_info(csv_files_path, table_number):
  try:
    tables_info = []
    with open(csv_files_path, mode='r', encoding='utf-8') as file:
      reader = csv.reader(file)
      #skips column header row
      next(reader)
      for data_row in reader:
        table_name = data_row[0] if len(data_row) > 0 else ''
        table_description = data_row[1] if len(data_row) > 1 else ''

        tables_info.append({
        #TO-DO: to match CSV file path of table name with the one in metadata folder
        "path": csv_files_path,
        #TO-DO: get full table name like TABLE_CATALOG.TABLE_SCHEMA.TABLE_NAME instead of just TABLE_NAME
        "table_name": table_name,
        "table_number": table_number,
        "table_header": table_name,
        "table_description": table_description
        })
        table_number += 1

  except Exception as e:
    print(f"Error - {e}")
    return None
  
  return tables_info

def create_json(tables_info):
  try:
    with open('tables_info_TEST.json', 'w',encoding='utf-8') as json_file:
      json.dump(tables_info,json_file,indent=4)
    print("Done")
  except Exception as e:
    print(f"Error - {e}")


def main():

  try:
    csv_metadata_folder = '/Users/alyssapineda/feature-copilot/feature-copilot/metadata'
    csv_files_folder = '/Users/alyssapineda/feature-copilot/feature-copilot/csv'


    all_tables_info = []
    table_number = 0

    for filename in os.listdir(csv_files_folder):
      if filename.endswith('.csv'):
        csv_files_path = os.path.join(csv_files_folder, filename)

        tables_info = get_table_info(csv_files_path, table_number)
        all_tables_info.extend(tables_info)
        table_number += 1

        create_json(tables_info)
  except Exception as e:
    print(f"Error - {e}")



if __name__ == "__main__":
  main()

