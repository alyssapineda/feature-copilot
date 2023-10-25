from langchain_utils import chain as chain_utils
from snowflake import snowflake_connect_test
from snowflake.snowpark.exceptions import SnowparkSQLException
from supabase_utils import supabase_connect, ingest
from utils.snowddls import Snowddl
from utils.snowchat_ui import StreamlitUICallbackHandler, message_func
from utils.snow_connect import SnowflakeConnection

import chat_bot
import streamlit as st
import utils.constants as constants
import warnings

def main():
    warnings.filterwarnings("ignore")
    chat_history = []
    snow_ddl = Snowddl()

    # Setup UI and chat
    chat_bot.initialise_ui(snow_ddl)
    chat_bot.initialise_chat()

    # Prompt for user input and save
    if prompt := st.chat_input():
        st.session_state.messages.append({"role": "user", "content": prompt})

    for message in st.session_state.messages:
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
            # if get_sql(result):
            #     conn = SnowflakeConnection().get_session()
            #     df = execute_sql(get_sql(result), conn)
            #     if df is not None:
            #         callback_handler.display_dataframe(df)
            #         append_message(df, "data", True)

    # snow = snow_connect.SnowflakeConnection()
    # connection = snow.get_session()
    # print(connection)

if __name__ == "__main__":
    main()
