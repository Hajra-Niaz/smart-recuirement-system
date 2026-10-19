import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'smart-recruitment-ai-system-2024')
    UPLOAD_FOLDER = 'static/uploads'
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024
    ALLOWED_EXTENSIONS = {'pdf', 'docx', 'txt', 'wav', 'mp3', 'm4a'}
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')