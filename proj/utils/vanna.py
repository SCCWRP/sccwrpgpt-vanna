import os

# Vanna AI imports
from vanna.openai.openai_chat import OpenAI_Chat
from vanna.chromadb.chromadb_vector import ChromaDB_VectorStore


class MyVanna(ChromaDB_VectorStore, OpenAI_Chat):
    def __init__(self, config=None):
        ChromaDB_VectorStore.__init__(self, config=config)
        OpenAI_Chat.__init__(self, config=config)
vn = MyVanna(config={'api_key': os.getenv('OPENAI_API_KEY'), 'model': os.getenv('OPENAI_MODEL')})

vn.connect_to_postgres(host=os.getenv("DB_HOST"), dbname=os.getenv("DB_NAME"), user=os.getenv("DB_USER"), password=os.getenv("DB_PASSWORD"), port=os.getenv("DB_PORT"))

