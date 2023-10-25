from typing import Any, Dict
import toml
import streamlit as st
from snowflake.snowpark.session import Session
from snowflake.snowpark.version import VERSION
from os_secrets import get_secrets_path
import snowflake.connector


class SnowflakeConnection:
    def __init__(self):
        self.connection_parameters = self.get_credentials() #self._get_connection_parameters_from_env()
        self.session = None

    @staticmethod
    def get_credentials():
        try:
            secrets = toml.load(get_secrets_path())
            snowflake_credentials = secrets.get("snowflake",{})
            return snowflake_credentials
        except Exception as e: 
            print("Error: ",e)
            return None

    # @staticmethod
    # def _get_connection_parameters_from_env() -> Dict[str, Any]:
    #     connection_parameters = {
    #         "account": st.secrets["SNOWFLAKE_ACCOUNT"],
    #         "user": st.secrets["SNOWFLAKE_USER"],
    #         "password": st.secrets["SNOWFLAKE_PASSWORD"],
    #         "warehouse": st.secrets["SNOWFLAKE_WAREHOUSE"],
    #         "database": st.secrets["SNOWFLAKE_DATABASE"],
    #         "schema": st.secrets["SNOWFLAKE_SCHEMA"],
    #         "role": st.secrets["SNOWFLAKE_ROLE"],
    #     }
    #     return connection_parameters
        
    
    def get_session(self):
        if self.session is None:
            # self.session = Session.builder.configs(self.connection_parameters).create()
            # self.session.sql_simplifier_enabled = True
            return snowflake.connector.connect(
                user=self.connection_parameters['SNOWFLAKE_USER'],
                password=self.connection_parameters['SNOWFLAKE_PASSWORD'],
                account=self.connection_parameters['SNOWFLAKE_ACCOUNT'],
                warehouse=self.connection_parameters['SNOWFLAKE_WAREHOUSE'],
                database=self.connection_parameters['SNOWFLAKE_DATABASE'],
                schema=self.connection_parameters['SNOWFLAKE_SCHEMA']
            )
        return self.session
    