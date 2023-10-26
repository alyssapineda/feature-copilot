from utils.credentials import Credentials
import vecs

def create_supabase_client():
    credentials = Credentials.get_credentials()
    supabase_client = load_supabase(credentials)
    return supabase_client

def load_supabase(credentials):
    print("Establishing Connection...")
    supabase_client = vecs.create_client(credentials['SUPABASE_DB_CONNECTION'])
    print("Connection Established")
    return supabase_client
