import csv, json, os

#function to get table info from CSV files from csv folder
def get_table_info(csv_files_path, table_number):
  try:
    tables_info = []
    with open(csv_files_path, mode='r', encoding='utf-8') as file:
      reader = csv.reader(file)
      #skipping column header row
      next(reader)
      for row in reader:
        table_header = f"{row[1]}" if len(row) > 0 else ''
        table_name = f"{row[3]}.{row[4]}.{row[1]}" if len(row) > 0 else ''
        table_description = row[6] if len(row) > 1 else ''

        tables_info.append({
        #TO-DO: to match CSV file path of table name with the one in metadata folder
        "path": f"metadata/{table_name}.csv",
        "table_name": table_name,
        "table_number": table_number,
        "table_header": table_header,
        "table_description": table_description
        })
        table_number += 1

  except Exception as e:
    print(f"Error - {e}")
    return []
  
  return tables_info

def create_json(tables_info):
  try:
    with open('tables_info.json', 'w',encoding='utf-8') as json_file:
      json.dump(tables_info,json_file,indent=2)
    print("Done")
  except Exception as e:
    print(f"Error - {e}")


def main():
  try:
    csv_metadata_folder = 'metadata'
    csv_files_folder = 'csv'


    all_tables_info = []
    table_number = 1

    for filename in os.listdir(csv_files_folder):
      #to exclude .DS_store file
      if filename.endswith('.csv'):
        print(f"File to be processed - {filename}")
        csv_files_path = os.path.join(csv_files_folder, filename)

        tables_info = get_table_info(csv_files_path, table_number)
        if tables_info:
          all_tables_info.extend(tables_info)
          # Update table_number by the number of tables added
          table_number += len(tables_info)

    create_json(all_tables_info)
  except Exception as e:
    print(f"Error - {e}")


if __name__ == "__main__":
  main()

