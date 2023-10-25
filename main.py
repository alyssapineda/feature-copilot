from snowflake import snowflake_connect_test
from supabase_utils import supabase_connect, ingest
from utils import snow_connect
import streamlit as st
from utils.snowddls import Snowddl

INITIAL_MESSAGE = [
    {"role": "user", "content": "Hi!"},
    {
        "role": "assistant",
        "content": "Hey there, I'm your Features Copilot, your SQL-speaking sidekick, ready to chat up Snowflake and fetch answers faster than a snowball fight in summer! ❄️🔍",
    }
]

MODEL = "GPT-3.5"

## Test through here
def main():

    chat_history = []
    snow_ddl = Snowddl()

    # Setup UI and chat
    initialise_ui(snow_ddl)
    initialise_chat()

    # Prompt for user input and save
    if prompt := st.chat_input():
        st.session_state.messages.append({"role": "user", "content": prompt})


    # snow = snow_connect.SnowflakeConnection()
    # connection = snow.get_session()
    # print(connection)

def initialise_ui(ddl):
    st.title("Features Copilot")
    st.caption("SQL Query Gneration")
    # model = st.radio(
    #     "",
    #     options=["✨ GPT-3.5", "🐐 code-LLama", "♾️ Claude"],
    #     index=0,
    #     horizontal=True,
    # )

    with open("ui/sidebar.md", "r") as sidebar_file:
        sidebar_content = sidebar_file.read()

    with open("ui/styles.md", "r") as styles_file:
        styles_content = styles_file.read()

    
    # Display the DDL for the selected table
    st.sidebar.markdown(sidebar_content)

    # Create a sidebar with a dropdown menu
    selected_table = st.sidebar.selectbox(
        "Select a table:", options=list(ddl.ddl_dict.keys())
    )
    st.sidebar.markdown(f"### DDL for {selected_table} table")
    st.sidebar.code(ddl.ddl_dict[selected_table], language="sql")

    # Add a reset button
    if st.sidebar.button("Reset Chat"):
        for key in st.session_state.keys():
            del st.session_state[key]
        st.session_state["messages"] = INITIAL_MESSAGE
        st.session_state["history"] = []

    st.sidebar.markdown(
        "**Note:** <span style='color:red'>The snowflake data retrieval is disabled for now.</span>",
        unsafe_allow_html=True,
    )

    st.write(styles_content, unsafe_allow_html=True)

def initialise_chat():
    # Initialize the chat messages history
    if "messages" not in st.session_state.keys():
        st.session_state["messages"] = INITIAL_MESSAGE

    if "history" not in st.session_state:
        st.session_state["history"] = []

    if "model" not in st.session_state:
        st.session_state["model"] = MODEL


if __name__ == "__main__":
    main()
