import re
import streamlit as st
import utils.constants as constants
from snowflake.snowpark.exceptions import SnowparkSQLException
# from utils.snowchat_ui import StreamlitUICallbackHandler

# callback_handler = StreamlitUICallbackHandler()
# chain = chain_utils.load_chain(st.session_state["model"], callback_handler)


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
    # if st.sidebar.button("Reset Chat"):
    #     for key in st.session_state.keys():
    #         del st.session_state[key]
    #     st.session_state["messages"] = constants.INITIAL_MESSAGE
    #     st.session_state["history"] = []

    st.sidebar.markdown(
        "**Note:** <span style='color:red'>The snowflake data retrieval is disabled for now.</span>",
        unsafe_allow_html=True,
    )

    st.write(styles_content, unsafe_allow_html=True)

def initialise_chat():
    # Initialize the chat messages history
    if "messages" not in st.session_state.keys():
        st.session_state["messages"] = constants.INITIAL_MESSAGE

    if "history" not in st.session_state:
        st.session_state["history"] = []

    if "model" not in st.session_state:
        st.session_state["model"] = constants.OPENAI["MODEL_NAME"]

def append_chat_history(question, answer):
    st.session_state["history"].append((question, answer))


def get_sql(text):
    sql_match = re.search(r"```sql\n(.*)\n```", text, re.DOTALL)
    return sql_match.group(1) if sql_match else None


def append_message(content, callback_handler, role="assistant", display=False):
    message = {"role": role, "content": content}
    st.session_state.messages.append(message)
    if role != "data":
        append_chat_history(st.session_state.messages[-2]["content"], content)

    if callback_handler.has_streaming_ended:
        callback_handler.has_streaming_ended = False
        return


# def handle_sql_exception(query, conn, e, retries=2):
#     append_message("Uh oh, I made an error, let me try to fix it..")
#     error_message = (
#         "You gave me a wrong SQL. FIX The SQL query by searching the schema definition:  \n```sql\n"
#         + query
#         + "\n```\n Error message: \n "
#         + str(e)
#     )
#     new_query = chain({"question": error_message, "chat_history": ""})["answer"]
#     append_message(new_query)
#     if get_sql(new_query) and retries > 0:
#         return execute_sql(get_sql(new_query), conn, retries - 1)
#     else:
#         append_message("I'm sorry, I couldn't fix the error. Please try again.")
#         return None


# def execute_sql(query, conn, retries=2):
#     if re.match(r"^\s*(drop|alter|truncate|delete|insert|update)\s", query, re.I):
#         append_message("Sorry, I can't execute queries that can modify the database.")
#         return None
#     try:
#         # return conn.sql(query).collect()
#         return conn.cursor.execute(query)

#     except SnowparkSQLException as e:
#         # return handle_sql_exception(query, conn, e, retries)
#         return f"Error: {str(e)}"