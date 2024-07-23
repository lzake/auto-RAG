# app/models/document_model.py
from pydantic import BaseModel

class DocumentUploadResponse(BaseModel):
    filename: str
    file_path: str

class GenerateResponseRequest(BaseModel):
    doc: str

class GenerateResponse(BaseModel):
    response: str

class RetrieveDocsRequest(BaseModel):
    query: str

class RetrieveDocsResponse(BaseModel):
    documents: list[str]
