import chain as chain_utils
from snowflake.snowpark.exceptions import SnowparkSQLException
from utils import snowflake_connect_test
from utils import supabase_connect, ingest
from utils.snowddls import Snowddl
from utils.snowchat_ui import StreamlitUICallbackHandler, message_func
from utils.snow_connect import SnowflakeConnection
import pandas as pd

import chat_bot
import streamlit as st
import warnings

# def execute_sql(query, conn, retries=2):
#     if re.match(r"^\s*(drop|alter|truncate|delete|insert|update)\s", query, re.I):
#         chat_bot.append_message("Sorry, I can't execute queries that can modify the database.")
#         return None
#     try:
#         cursor = conn.cursor()
#         return cursor.execute(query)

#     except SnowparkSQLException as e:
#         # return handle_sql_exception(query, conn, e, retries)
#         return f"Error: {str(e)}"

def main():
    warnings.filterwarnings("ignore")
    chat_history = []
    snow_ddl = Snowddl()

    # Setup UI and chat
    chat_bot.initialise_ui(snow_ddl)
    chat_bot.initialise_chat()

    # Prompt for user input and store in st.session_state.messages
    if prompt := st.chat_input():
        st.session_state.messages.append({"role": "user", "content": prompt})

    # Create the message bubbles in UI
    for message in st.session_state.messages:
        print(message)
        message_func(
            message["content"],
            True if message["role"] == "user" else False,
            True if message["role"] == "data" else False,
        )

    callback_handler = StreamlitUICallbackHandler()

    chain = chain_utils.load_chain(st.session_state["model"], callback_handler)

    if st.session_state.messages[-1]["role"] != "assistant":
        content = st.session_state.messages[-1]["content"]
        if isinstance(content, str):
            result = chain(
                {"question": content, "chat_history": st.session_state["history"]}
            )["answer"]
            print(result)
            chat_bot.append_message(result, callback_handler)
            #gets result and extract sql query and make snowflake connection
            if chat_bot.get_sql(result):
                conn = SnowflakeConnection().get_session()
                # print(result)
                start_string = result.find("```sql")+len("```sql")
                end_string = result.rfind("```")
                sql_query = result[start_string:end_string]
                print(sql_query)
                # cursor = conn.cursor()
                # cursor.execute(sql_query)
                # cursor.close()

                # df = chat_bot.execute_sql(chat_bot.get_sql(sql_query), conn)
                df = chat_bot.execute_sql(sql_query, conn)
                # print(type(df))
                if df is not None:
                    callback_handler.display_dataframe(df)
                    chat_bot.append_message(df, "data", True)
                else:
                    print("This is empty")
if __name__ == "__main__":
    main()
