from typing import Any, Callable, Dict, Optional
from os_secrets import get_secrets_path
from supabase_utils import supabase_connect
import toml
import boto3
import streamlit as st
import os
import vecs
import openai
from langchain.chains import ConversationalRetrievalChain, LLMChain
from langchain.chains.question_answering import load_qa_chain
from langchain.chat_models import ChatOpenAI
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.llms import OpenAI, Replicate
from langchain.llms.bedrock import Bedrock
from langchain.vectorstores import SupabaseVectorStore
from pydantic import BaseModel, validator
from supabase.client import Client, create_client

from template import CONDENSE_QUESTION_PROMPT, QA_PROMPT


# supabase_url=st.secrets["SUPABASE_URL"]
# supabase_service_key=st.secrets["SUPABASE_SERVICE_KEY"]

# supabase: Client = create_client(supabase_url, supabase_service_key)

def get_credentials():
    secrets_path = get_secrets_path()
    try:
        secrets = toml.load(secrets_path)
        supabase_credentials = secrets.get("supabase",{})
        return supabase_credentials
    except Exception as e: 
        print("Error: ",e)
        return None

def create_supabase_client(url, key):
  print("...Testing connectivity...")
  supabase: Client = create_client(url, key)
  print("...Connection Established...")
  return supabase

def get_chain(vectorstore):
  """
  Get chain for chatting with vector database  
  """

  q_llm = OpenAI(
    temperature = 0,
    openai_api_key=st.secrets["OPENAI_API_KEY"],
    model_name="gpt-3.5-turbo-16k",
  )

  llm = ChatOpenAI(
    temperature=0,
    openai_api_key=st.secrets["OPENAI_API_KEY"],
    model_name="gpt-3.5-turbo",
  )

  question_generator = LLMChain(llm=q_llm, prompt=CONDENSE_QUESTION_PROMPT)

  doc_chain = load_qa_chain(llm=llm, chain_type="stuff", prompt=QA_PROMPT)
  chain = ConversationalRetrievalChain(
      retriever=vectorstore.as_retriever(),
      combine_docs_chain=doc_chain,
      question_generator=question_generator,
  )
  return chain



def main():
  supabase_credentials = get_credentials()
  if supabase_credentials:
    result = create_supabase_client(
    supabase_credentials['SUPABASE_URL'],
    supabase_credentials['SUPABASE_SERVICE_KEY']        
    )
    print(result)

    # chain = get_chain(SupabaseVectorStore)
    # print(chain)

  else:
    print("Cannot retrieve credentials from secrets toml")

if __name__ == "__main__":
  main()