INITIAL_MESSAGE = [
    #{"role": "user", "content": "Hi!"},
    {
        "role": "assistant",
        "content": "Hey there, I'm your Features Copilot. Ask me a question about your data and I will generate a valid SQL statement. I will also execute the statement on your Snowflake data and return the result!",
    }
]

OPENAI = {
    "MODEL_NAME": "GPT-4",
    "EMBEDDING_MODEL": "text-embedding-ada-002"
}