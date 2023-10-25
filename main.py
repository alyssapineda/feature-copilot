from snowflake import snowflake_connect_test
from supabase_utils import supabase_connect, ingest

## Test through here
def main():

    #supabase_client = supabase_connect.create_supabase_client()

    print("Converting .md to vectors and storing in supabase")
    ingest.run()
    print("Successfully converted and stored in supabase")

    # snowflake_credentials = snowflake_connect_test.get_credentials()

    # if snowflake_credentials:
    #     result = snowflake_connect_test.test_snowflake_connection(
    #         snowflake_credentials['SNOWFLAKE_USER'],
    #         snowflake_credentials['SNOWFLAKE_PASSWORD'],
    #         snowflake_credentials['SNOWFLAKE_ACCOUNT'],
    #         snowflake_credentials['SNOWFLAKE_WAREHOUSE'],  
    #         snowflake_credentials['SNOWFLAKE_DATABASE'],
    #         snowflake_credentials['SNOWFLAKE_SCHEMA']            
    #     )
    #     print(result)
    # else:
    #     print("Unable to connect to snowflake.")

if __name__ == "__main__":
    main()
