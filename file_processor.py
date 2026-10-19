import os
import uuid
from werkzeug.utils import secure_filename
from config import Config

class FileProcessor:
    @staticmethod
    def allowed_file(filename):
        return '.' in filename and \
               filename.rsplit('.', 1)[1].lower() in Config.ALLOWED_EXTENSIONS
    
    @staticmethod
    def save_uploaded_file(file, upload_type='resume'):
        """Save uploaded file with unique filename"""
        if file and FileProcessor.allowed_file(file.filename):
            # Generate unique filename
            filename = f"{uuid.uuid4()}_{secure_filename(file.filename)}"
            
            if upload_type == 'resume':
                folder = 'static/uploads/resumes'
            else:  # interview
                folder = 'static/uploads/interviews'
            
            # Ensure directory exists
            os.makedirs(folder, exist_ok=True)
            
            filepath = os.path.join(folder, filename)
            file.save(filepath)
            return filepath
        
        return None
    
    @staticmethod
    def cleanup_file(filepath):
        """Remove file from filesystem"""
        try:
            if os.path.exists(filepath):
                os.remove(filepath)
                return True
        except:
            pass
        return False