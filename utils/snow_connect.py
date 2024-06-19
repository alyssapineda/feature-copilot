from typing import Any, Dict
from snowflake.snowpark.session import Session
from snowflake.snowpark.version import VERSION
from utils.credentials import Credentials
import snowflake.connector


class SnowflakeConnection:
    def __init__(self):
        self.connection_parameters = Credentials.get_credentials(section="snowflake")
        self.session = None

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

    def sql_execution(self):
        sql =""
        if self.session is None:
            cursor = conn.cursor()
            cursor.execute(sql)
            cursor.close()

# if __name__  == "__main__":

