from os_secrets import get_secrets_path
import streamlit as st
import snowflake.connector
import toml

def get_credentials():
    try:
        secrets = toml.load(get_secrets_path())
        snowflake_credentials = secrets.get("snowflake",{})
        return snowflake_credentials
    except Exception as e: 
        print("Error: ",e)
        return None

def test_snowflake_connection(username, password, account, warehouse, database, schema):
    try:
        conn = snowflake.connector.connect(
            user=username,
            password=password,
            account=account,
            warehouse=warehouse,
            database=database,
            schema=schema
        )
        cursor = conn.cursor()
        
        cursor.execute("SELECT CURRENT_USER()")
        current_user = cursor.fetchone()[0]
        print(f"Current user: {current_user}")

        cursor.execute("SELECT CURRENT_DATABASE()")
        current_db = cursor.fetchone()[0]
        print(f"Current database: {current_db}")

        cursor.execute("SELECT CURRENT_SCHEMA()")
        current_schema = cursor.fetchone()[0]
        print(f"Current database: {current_schema}")

        cursor.execute("SELECT CURRENT_ROLE()")
        result = cursor.fetchone()
        return f"Connected to Snowflake using current role: {result[0]}"
    except Exception as e:
        return f"Snowflake connection error: {str(e)}"
