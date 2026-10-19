class AIModelsConfig:
    """Configuration for various AI models used in the system"""
    
    # OpenAI Models
    OPENAI_MODELS = {
        "resume_analysis": "gpt-3.5-turbo",
        "interview_analysis": "gpt-3.5-turbo",
        "scoring": "gpt-3.5-turbo"
    }
    
    # Analysis Prompts
    RESUME_ANALYSIS_PROMPT = """
    Analyze this resume for a {job_title} position and provide a comprehensive evaluation.
    
    Resume Text: {resume_text}
    
    Please provide analysis in this JSON format:
    {{
        "skills_match": {{
            "matched_skills": ["skill1", "skill2"],
            "missing_skills": ["skill3", "skill4"],
            "match_percentage": 75
        }},
        "experience_analysis": {{
            "relevant_experience": "Description of relevant experience",
            "experience_level": "Junior/Mid/Senior",
            "score": 80
        }},
        "education_analysis": {{
            "qualifications": "Education summary",
            "score": 85
        }},
        "overall_score": 78,
        "strengths": ["Strength1", "Strength2"],
        "weaknesses": ["Weakness1", "Weakness2"],
        "recommendations": ["Recommendation1", "Recommendation2"]
    }}
    """
    
    INTERVIEW_ANALYSIS_PROMPT = """
    Analyze this interview Q&A and provide comprehensive evaluation:
    
    Interview Data: {interview_data}
    
    Provide analysis in this JSON format:
    {{
        "communication_skills": {{
            "clarity": 85,
            "confidence": 78,
            "articulation": 82,
            "overall_score": 82
        }},
        "technical_knowledge": {{
            "depth": 88,
            "accuracy": 85,
            "relevance": 90,
            "overall_score": 88
        }},
        "problem_solving": {{
            "approach": 80,
            "creativity": 75,
            "efficiency": 82,
            "overall_score": 79
        }},
        "cultural_fit": {{
            "values_alignment": 85,
            "teamwork": 80,
            "adaptability": 78,
            "overall_score": 81
        }},
        "overall_score": 82,
        "strengths": ["Good technical knowledge", "Clear communication"],
        "weaknesses": ["Could improve problem-solving", "Need more confidence"],
        "recommendations": ["Provide technical training", "Practice interview skills"]
    }}
    """