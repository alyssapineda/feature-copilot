import platform
import toml

class Credentials:

    @staticmethod
    def get_secrets_path():
        if platform.system() == 'Windows':
            return '.streamlit\secrets.toml'
        return '.streamlit/secrets.toml'
    
    @staticmethod
    def get_csv_path(filename=None):
        if platform.system() == 'Windows':
            return 'csv\\fred_financial_labor_performance.csv' if filename is None else 'csv\\' +  filename
        return 'csv/fred_financial_labor_performance.csv' if  filename is None else 'csv/' + filename

    @staticmethod
    def get_credentials(section=None):
        secrets_path = Credentials.get_secrets_path()
        try:
            secrets = toml.load(secrets_path)
            return secrets if section is None else secrets.get(section, {})
        except Exception as e: 
            print("Error: ", e)
            return None