from flask import Flask, render_template, request, jsonify, session, redirect, url_for, send_from_directory
import os
from werkzeug.utils import secure_filename
from models.resume_analyzer import ResumeAnalyzer
from models.interview_analyzer import InterviewAnalyzer
from models.score_calculator import ScoreCalculator
import uuid
import json

# Initialize Flask app
app = Flask(__name__)
app.config.from_object('config.Config')

# Ensure upload directories exist
os.makedirs('static/uploads/resumes', exist_ok=True)
os.makedirs('static/downloads', exist_ok=True)

def allowed_file(filename):
    allowed_extensions = {'pdf', 'docx', 'txt'}
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in allowed_extensions

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/resume-reader')
def resume_reader():
    return render_template('resume_reader.html')

@app.route('/analyze-resume', methods=['POST'])
def analyze_resume():
    try:
        if 'resume' not in request.files:
            return jsonify({'error': 'No file uploaded'}), 400
        
        file = request.files['resume']
        job_title = request.form.get('job_title', '').strip()
        
        if not job_title:
            return jsonify({'error': 'Job title is required'}), 400
        
        if file.filename == '':
            return jsonify({'error': 'No file selected'}), 400
        
        if file and allowed_file(file.filename):
            filename = f"{uuid.uuid4()}_{secure_filename(file.filename)}"
            filepath = os.path.join('static/uploads/resumes', filename)
            file.save(filepath)
            
            analyzer = ResumeAnalyzer()
            result = analyzer.analyze_resume(filepath, job_title)
            
            session['resume_analysis'] = result
            
            return jsonify({
                'status': 'success',
                'message': 'Resume analyzed successfully with AI!',
                'redirect': '/interview-analyzer'
            })
        else:
            return jsonify({'error': 'Invalid file type. Please upload PDF, DOCX, or TXT.'}), 400
        
    except Exception as e:
        return jsonify({'error': f'Analysis failed: {str(e)}'}), 500

@app.route('/interview-analyzer')
def interview_analyzer():
    return render_template('interview_analyzer.html')

@app.route('/manual-interview')
def manual_interview():
    return render_template('manual_interview.html')

@app.route('/analyze-manual-interview', methods=['POST'])
def analyze_manual_interview():
    try:
        data = request.get_json()
        
        if not data or 'questions_answers' not in data:
            return jsonify({'error': 'No interview data provided'}), 400
        
        questions_answers = data.get('questions_answers', [])
        
        if not questions_answers:
            return jsonify({'error': 'No questions and answers provided'}), 400
        
        analyzer = InterviewAnalyzer()
        result = analyzer.analyze_text_interview(questions_answers)
        
        session['interview_analysis'] = result
        
        return jsonify({
            'status': 'success', 
            'message': 'Interview analyzed successfully with AI!',
            'redirect': '/results'
        })
        
    except Exception as e:
        return jsonify({'error': f'Interview analysis failed: {str(e)}'}), 500

@app.route('/results')
def show_results():
    try:
        resume_analysis = session.get('resume_analysis')
        interview_analysis = session.get('interview_analysis')
        
        if not resume_analysis:
            return redirect('/resume-reader')
        
        if not interview_analysis:
            return redirect('/interview-analyzer')
        
        score_calculator = ScoreCalculator()
        final_result = score_calculator.calculate_final_score(resume_analysis, interview_analysis)
        
        return render_template('results.html', 
                             resume_analysis=resume_analysis,
                             interview_analysis=interview_analysis,
                             final_result=final_result)
                             
    except Exception as e:
        return f"Error displaying results: {str(e)}"

@app.route('/view-results')
def view_results():
    return redirect('/results')

@app.route('/clear-session')
def clear_session():
    session.clear()
    return "Session cleared"

# --- THIS IS THE ONLY PART CHANGED FOR RENDER ---
if __name__ == '__main__':
    # Render provides a PORT environment variable
    port = int(os.environ.get('PORT', 5000))
    # Turn off debug for production
    app.run(host='0.0.0.0', port=port, debug=False)