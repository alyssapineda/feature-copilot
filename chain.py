from langchain.chains import ConversationalRetrievalChain, LLMChain
from langchain.chains.question_answering import load_qa_chain
from langchain.chat_models import ChatOpenAI
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import SupabaseVectorStore
from pydantic import BaseModel, validator
from supabase import create_client, Client
import template
from typing import Any, Callable, Dict, Optional
from utils.credentials import Credentials

import utils.constants as constants
import streamlit as st

class ModelConfig(BaseModel):
    model_type: str
    secrets: Dict[str, Any]
    callback_handler: Optional[Callable] = None

    @validator("model_type", pre=True, always=True)
    def validate_model_type(cls, v):
        if v not in ["code-llama", "gpt", "claude"]:
            raise ValueError(f"Unsupported model type: {v}")
        return v

class ModelWrapper:
    def __init__(self, config: ModelConfig):
        self.model_type = config.model_type
        self.secrets = Credentials.get_credentials()
        self.callback_handler = config.callback_handler
        self.setup()

    def setup(self):
      self.setup_gpt()

    def setup_gpt(self):
        self.q_llm = ChatOpenAI(
            temperature=0.5,
            openai_api_key=self.secrets["OPENAI_API_KEY"],
            model_name="gpt-3.5-turbo-16k",
            max_tokens=500,
        )

        self.llm = ChatOpenAI(
            model_name="gpt-3.5-turbo-16k",
            temperature=0.5,
            openai_api_key=self.secrets["OPENAI_API_KEY"],
            max_tokens=500,
            callbacks=[self.callback_handler],
            streaming=True,
        )

    def get_chain(self, vectorstore):
        if not self.q_llm or not self.llm:
            raise ValueError("Models have not been properly initialized.")
        question_generator = LLMChain(llm=self.q_llm, prompt=template.CONDENSE_QUESTION_PROMPT)
        doc_chain = load_qa_chain(llm=self.llm, chain_type="stuff", prompt=template.QA_PROMPT)
        conv_chain = ConversationalRetrievalChain(
            retriever=vectorstore.as_retriever(),
            combine_docs_chain=doc_chain,
            question_generator=question_generator,
        )
        return conv_chain

def load_chain(model_name=constants.OPENAI["MODEL_NAME"], callback_handler=None):
    supabase_credentials = Credentials.get_credentials(section="supabase")
    supabase_url = supabase_credentials["SUPABASE_URL"]
    supabase_key = supabase_credentials["SUPABASE_API_KEY"]
    supabase_client: Client = create_client(supabase_url, supabase_key)

    embeddings = OpenAIEmbeddings(
        openai_api_key=st.secrets["OPENAI_API_KEY"], model=constants.OPENAI["EMBEDDING_MODEL"]
    )
    vectorstore = SupabaseVectorStore(
        embedding=embeddings,
        client=supabase_client,
        table_name="documents",
        query_name="v_match_documents",
    )

    if "claude" in model_name.lower():
        model_type = "claude"
    elif "GPT-3.5" in model_name:
        model_type = "gpt"
    else:
        model_type = "code-llama"

    config = ModelConfig(
        model_type=model_type, secrets=st.secrets, callback_handler=callback_handler
    )
    model = ModelWrapper(config)
    return model.get_chain(vectorstore)


# def get_chain(vectorstore):
#   """
#   Get chain for chatting with vector database  
#   """

#   q_llm = OpenAI(
#     temperature = 0,
#     openai_api_key=st.secrets["OPENAI_API_KEY"],
#     model_name="gpt-3.5-turbo-16k",
#   )

#   llm = ChatOpenAI(
#     temperature=0,
#     openai_api_key=st.secrets["OPENAI_API_KEY"],
#     model_name="gpt-3.5-turbo",
#   )

#   question_generator = LLMChain(llm=q_llm, prompt=CONDENSE_QUESTION_PROMPT)

#   doc_chain = load_qa_chain(llm=llm, chain_type="stuff", prompt=QA_PROMPT)
#   chain = ConversationalRetrievalChain(
#       retriever=vectorstore.as_retriever(),
#       combine_docs_chain=doc_chain,
#       question_generator=question_generator,
#   )
#   return chain




  # supabase_credentials = get_credentials()
  # if supabase_credentials:
  #   result = create_supabase_client(
  #   supabase_credentials['SUPABASE_URL'],
  #   supabase_credentials['SUPABASE_SERVICE_KEY']        
  #   )
  #   print(result)

    # chain = get_chain(SupabaseVectorStore)
    # print(chain)

  # else:
  #   print("Cannot retrieve credentials from secrets toml")

# if __name__ == "__main__":
#     load_chain()