import html
import re
import pandas as pd

import streamlit as st
from langchain.callbacks.base import BaseCallbackHandler


def format_message(text):
    text_blocks = re.split(r"```[\s\S]*?```", text)
    code_blocks = re.findall(r"```([\s\S]*?)```", text)

    text_blocks = [html.escape(block) for block in text_blocks]

    formatted_text = ""
    for i in range(len(text_blocks)):
        formatted_text += text_blocks[i].replace("\n", "<br>")
        if i < len(code_blocks):
            formatted_text += f'<pre style="white-space: pre-wrap; word-wrap: break-word;"><code>{html.escape(code_blocks[i])}</code></pre>'

    return formatted_text


def message_func(text, is_user=False, is_df=False, data=None):
    if is_user:
        avatar_url = "https://icons.veryicon.com/png/o/miscellaneous/forestry-in-yiliang/person-11.png"
        message_alignment = "flex-end"
        message_bg_color = "#FFF5CC"
        text_color = "#000000"
        avatar_class = "user-avatar"
        st.write(
            f"""
                <div style="display: flex; align-items: center; margin-bottom: 10px; justify-content: {message_alignment};">
                    <div style="background:{message_bg_color}; color:{text_color}; border: solid thin #F2C78C; border-radius: 20px; padding: 10px; margin-right: 5px; max-width: 75%; font-size: 17px;">
                        {text} \n </div>
                    <img src="{avatar_url}" class="{avatar_class}" alt="avatar" style="width: 50px; height: 50px;" />
                </div>
                """,
            unsafe_allow_html=True,
        )
    else:
        avatar_url = "https://icons.veryicon.com/png/o/object/material-design-icons-1/robot-13.png"
        message_alignment = "flex-start"
        message_bg_color = "#F2F2F1"
        text_color = "#000000"
        avatar_class = "bot-avatar"

        if is_df:# or isinstance(text, pd.DataFrame):
        #if is_df or type(text) == "<class 'pandas.core.frame.DataFrame'>":
        # if is_df == type(text):

            # st.write(
            #     f"""
            #         <div style="display: flex; align-items: center; margin-bottom: 10px; justify-content: {message_alignment};">
            #             <img src="{avatar_url}" class="{avatar_class}" alt="avatar" style="width: 50px; height: 50px;" />
            #             <div style="background: {message_bg_color}; color: {text_color}; border: solid thin #BEBEB9; border-radius: 20px; padding: 10px; margin-right: 5px; max-width: 75%; font-size: 17px;">
            #             {text} \n </div>
            #         </div>
            #         """,
            #     unsafe_allow_html=True,
            # )
            # st.write(text)
            display_dataframe(pd.DataFrame(data))
            return
        else:
            text = format_message(text)

            st.write(
                f"""
                    <div style="display: flex; align-items: center; margin-bottom: 10px; justify-content: {message_alignment};">
                        <img src="{avatar_url}" class="{avatar_class}" alt="avatar" style="width: 50px; height: 50px;" />
                        <div style="background: {message_bg_color}; color: {text_color}; border-radius: 20px; padding: 10px; margin-right: 5px; max-width: 75%; font-size: 17px;">
                            {text} \n </div>
                    </div>
                    """,
                unsafe_allow_html=True,
            )


def display_dataframe(df):
    avatar_url = "https://icons.veryicon.com/png/o/object/material-design-icons-1/robot-13.png"
    message_alignment = "flex-start"
    avatar_class = "bot-avatar"

    st.write(
        f"""
        <div style="display: flex; align-items: center; margin-bottom: 10px; justify-content: {message_alignment};">
            <img src="{avatar_url}" class="{avatar_class}" alt="avatar" style="width: 50px; height: 50px;" />
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.write(df)

class StreamlitUICallbackHandler(BaseCallbackHandler):
    def __init__(self):
        # Buffer to accumulate tokens
        self.token_buffer = []
        self.placeholder = None
        self.has_streaming_ended = False

    def _get_bot_message_container(self, text):
        avatar_url = "https://icons.veryicon.com/png/o/object/material-design-icons-1/robot-13.png"
        message_alignment = "flex-start"
        message_bg_color = "#F2F2F1"
        text_color = "#000000"
        avatar_class = "bot-avatar"
        formatted_text = format_message(text)
        container_content = f"""
            <div style="display: flex; align-items: center; margin-bottom: 10px; justify-content: {message_alignment};">
                <img src="{avatar_url}" class="{avatar_class}" alt="avatar" style="width: 50px; height: 50px;" />
                <div style="background: {message_bg_color}; color: {text_color}; border-radius: 20px; padding: 10px; margin-right: 5px; max-width: 75%; font-size: 17px;">
                    {formatted_text} \n </div>
            </div>
        """
        return container_content

    def on_llm_new_token(self, token, run_id, parent_run_id=None, **kwargs):
        self.token_buffer.append(token)
        complete_message = "".join(self.token_buffer)
        if self.placeholder is None:
            container_content = self._get_bot_message_container(complete_message)
            self.placeholder = st.markdown(container_content, unsafe_allow_html=True)
        else:
            # Update the placeholder content
            container_content = self._get_bot_message_container(complete_message)
            self.placeholder.markdown(container_content, unsafe_allow_html=True)

    # def display_dataframe(self, df):
    #     avatar_url = "https://icons.veryicon.com/png/o/object/material-design-icons-1/robot-13.png"
    #     message_alignment = "flex-start"
    #     avatar_class = "bot-avatar"

    #     st.write(
    #         f"""
    #         <div style="display: flex; align-items: center; margin-bottom: 10px; justify-content: {message_alignment};">
    #             <img src="{avatar_url}" class="{avatar_class}" alt="avatar" style="width: 50px; height: 50px;" />
    #         </div>
    #         """,
    #         unsafe_allow_html=True,
    #     )
    #     st.write(df)

    def on_llm_end(self, response, run_id, parent_run_id=None, **kwargs):
        self.token_buffer = []  # Reset the buffer
        self.has_streaming_ended = True

    def __call__(self, *args, **kwargs):
        pass