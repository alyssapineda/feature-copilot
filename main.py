import chain as chain_utils
from snowflake.snowpark.exceptions import SnowparkSQLException
from utils.snowddls import Snowddl
from utils.snowchat_ui import StreamlitUICallbackHandler, message_func, display_dataframe
from utils.snow_connect import SnowflakeConnection
import pandas as pd

import chat_bot
import streamlit as st
import warnings
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

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

    with open("ui/styling.css") as css:
        st.markdown(f'<style>{css.read()}</style>', unsafe_allow_html=True)

    # Prompt for user input and store in st.session_state.messages
    if prompt := st.chat_input():
        st.session_state.messages.append({"role": "user", "content": prompt})

    # Create the message bubbles in UI
    for message in st.session_state.messages:
        print(message)
        logger.info(message)
        try:
            dataframe = message["dataframe"]
        except:
            dataframe = None
        message_func(
            message["content"],
            True if message["role"] == "user" else False,
            True if message["role"] == "data" else False,
            dataframe
        )

    callback_handler = StreamlitUICallbackHandler()

    chain = chain_utils.load_chain(st.session_state["model"], callback_handler)
    logger.info("....Execute chain....")

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
                logger.info(sql_query)
                cursor = conn.cursor()
                sql_result = cursor.execute(sql_query).fetchall()
                print("RESULT")
                print(sql_result)
                cursor.close()

                df = pd.DataFrame(sql_result)

                #df = chat_bot.execute_sql(chat_bot.get_sql(sql_query), conn)
                #df = chat_bot.execute_sql(sql_query, conn)
                #df = chat_bot.execute_sql(sql_query)
                #df = chat_bot.get_sql(sql_query)
                print(type(df))
                if df is not None:
                    display_dataframe(df)
                    chat_bot.append_message(df, role="data", display=True)
                else:
                    print("This is empty")
if __name__ == "__main__":
    main()
