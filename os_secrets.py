import platform

def get_secrets_path():
    if platform.system() == 'Windows':
        return '.streamlit\secrets.toml'
    return '.streamlit/secrets.toml'