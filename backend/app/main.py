import logging
import chardet
from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from app.services.document_service import DocRetrievalService, DocGenerationService
from app.models.document_model import GenerateResponse, RetrieveDocsResponse
import os

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Adjust this to your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/api/upload", response_model=GenerateResponse)
async def upload_file(file: UploadFile = File(...)):
    try:
        logger.debug(f"Received file: {file.filename}")
        content = await file.read()
        logger.debug(f"File size: {len(content)} bytes")
        
        # Detect file encoding
        result = chardet.detect(content)
        encoding = result.get('encoding')
        logger.debug(f"Detected file encoding: {encoding}")
        
        if not encoding:
            encoding = 'utf-8'  # Fallback to utf-8 if encoding detection fails
            logger.debug("Falling back to utf-8 encoding")

        decoded_content = content.decode(encoding, errors='replace')
        
        file_path = f"./uploaded_files/{file.filename}"
        with open(file_path, "wb") as f:
            f.write(content)
        
        # Directly generate response using the file content
        generator = DocGenerationService()
        logger.debug("Calling generate function with file content")
        response = generator.generate(decoded_content)  # Use decoded content as string
        logger.debug(f"Generated response: {response}")
        
        return {"response": response}
    except Exception as e:
        logger.error(f"Error processing file: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/retrieve-docs", response_model=RetrieveDocsResponse)
async def retrieve_docs(query: str):
    retriever = DocRetrievalService()
    docs = retriever.retrieve(query)
    return {"documents": docs}

if not os.path.exists("./uploaded_files"):
    os.makedirs("./uploaded_files")
