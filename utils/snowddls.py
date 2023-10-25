class Snowddl:
    def __init__(self):
        self.ddl_dict = self.load_ddls()

    @staticmethod
    def load_ddls():
        ddl_files = {
            "FDIC": "sql/select_fdic.sql",
            "FRED FINANCIAL LABOUR PERFORMANCE": "sql/select_fred_financial_labour.sql",
            "FRED INTEREST DATA": "sql/select_fred_interest_data.sql",
            "FRED UNEPLOYMENT": "sql/select_fred_unemployment.sql",
            "NCUA CREDIT": "sql/select_ncua_credit.sql",
        }

        ddl_dict = {}
        for table_name, file_name in ddl_files.items():
            with open(file_name, "r") as f:
                ddl_dict[table_name] = f.read()
        return ddl_dict