import os_secrets
import toml
import vecs

def create_supabase_client():
    credentials = get_credentials()
    supabase_client = load_supabase(credentials)
    return supabase_client

def get_credentials():
    secrets_path = os_secrets.get_secrets_path()
    try:
        secrets = toml.load(secrets_path)
        supabase_credentials = secrets.get("supabase",{})
        return supabase_credentials
    except Exception as e: 
        print("Error: ",e)
        return None

def load_supabase(credentials):
    print("Establishing Connection...")
    supabase_client = vecs.create_client(credentials['SUPABASE_DB_CONNECTION'])
    print("Connection Established")
    return supabase_client
