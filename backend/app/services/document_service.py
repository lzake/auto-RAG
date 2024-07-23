import openai
from dotenv import load_dotenv
import os
import time

load_dotenv()

class DocGenerationService:
    def __init__(self):
        openai.api_key = os.getenv('OPENAI_API_KEY')
    
    def generate(self, doc):
        max_chunk_size = 4000
        chunks = [doc[i:i + max_chunk_size] for i in range(0, len(doc), max_chunk_size)]

        responses = []
        for chunk in chunks:
            retry_attempts = 5
            for attempt in range(retry_attempts):
                try:
                    response = openai.ChatCompletion.create(
                        model="gpt-4",
                        messages=[
                            {"role": "system", "content": "You are a helpful assistant."},
                            {"role": "user", "content": chunk}
                        ],
                        max_tokens=150
                    )
                    responses.append(response.choices[0].message['content'])
                    break
                except openai.error.RateLimitError as e:
                    if attempt < retry_attempts - 1:
                        wait_time = 2 ** attempt
                        time.sleep(wait_time)
                    else:
                        raise e
                except openai.error.OpenAIError as e:
                    raise e
        
        return " ".join(responses)

class DocRetrievalService:
    def __init__(self):
        self.index = DocumentIndex()
    
    def retrieve(self, query):
        self.load_documents()
        return self.index.search(query)
    
    def load_documents(self):
        self.documents = []
        file_path = './uploaded_files/rfp_example.pdf'
        if os.path.exists(file_path):
            with open(file_path, 'rb') as file:
                self.documents.append(file.read())
