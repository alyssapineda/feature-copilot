import os_secrets
import toml
import vecs

def load_supabase():
    credentials = get_credentials()
    supabase_client = create_supabase_client(credentials)

    table = supabase_client.get_or_create_collection(name="public.test_db", dimension=3)
    print("Loaded table")

def get_credentials():
    secrets_path = os_secrets.get_secrets_path()
    try:
        secrets = toml.load(secrets_path)
        supabase_credentials = secrets.get("supabase",{})
        return supabase_credentials
    except Exception as e: 
        print("Error: ",e)
        return None

def create_supabase_client(credentials):
    print("Establishing Connection...")
    supabase_client = vecs.create_client(credentials['SUPABASE_DB_CONNECTION'])
    print("Connection Established")
    return supabase_client
