from typing import Any, Dict

import streamlit as st
from snowflake.snowpark.session import Session
from snowflake.snowpark.version import VERSION



class SnowflakeConnection:
    def __init__(self):
        self.connection_parameters = self._get_connection_parameters_from_env()
        self.session = None

    @staticmethod
    def _get_connection_parameters_from_env() -> Dict[str, Any]:
        connection_parameters = {
            "account": st.secrets["SNOWFLAKE_ACCOUNT"],
            "user": st.secrets["SNOWFLAKE_USER"],
            "password": st.secrets["SNOWFLAKE_PASSWORD"],
            "warehouse": st.secrets["SNOWFLAKE_WAREHOUSE"],
            "database": st.secrets["SNOWFLAKE_DATABASE"],
            "schema": st.secrets["SNOWFLAKE_SCHEMA"],
            "role": st.secrets["SNOWFLAKE_ROLE"],
        }
        return connection_parameters
        
    
    def get_session(self):
        if self.session is None:
            self.session = Session.builder.configs(self.connection_parameters).create()
            self.session.sql_simplifier_enabled = True
        return self.session
    