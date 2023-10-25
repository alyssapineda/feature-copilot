import toml
import vecs

def get_credentials():
    secrets_path = '.streamlit\secrets.toml'
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

def main():
    credentials = get_credentials()
    supabase_client = create_supabase_client(credentials)

    table = supabase_client.get_or_create_collection(name="public.test_db", dimension=3)
    print("Loaded table")


if __name__ == "__main__":
    main()