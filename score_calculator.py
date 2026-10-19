class ScoreCalculator:
    def calculate_final_score(self, resume_analysis, interview_analysis):
        try:
            # Extract scores safely
            resume_score = resume_analysis.get('analysis', {}).get('overall_score', 0)
            interview_score = interview_analysis.get('analysis', {}).get('overall_score', 0)
            
            # If scores are 0, try to calculate from sub-scores
            if resume_score == 0 and 'analysis' in resume_analysis:
                resume_analysis_data = resume_analysis['analysis']
                skills_score = resume_analysis_data.get('skills_match', {}).get('match_percentage', 0)
                exp_score = resume_analysis_data.get('experience_analysis', {}).get('score', 0)
                edu_score = resume_analysis_data.get('education_analysis', {}).get('score', 0)
                resume_score = (skills_score + exp_score + edu_score) // 3
            
            if interview_score == 0 and 'analysis' in interview_analysis:
                interview_analysis_data = interview_analysis['analysis']
                comm_score = interview_analysis_data.get('communication_skills', {}).get('overall_score', 0)
                tech_score = interview_analysis_data.get('technical_knowledge', {}).get('overall_score', 0)
                prob_score = interview_analysis_data.get('problem_solving', {}).get('overall_score', 0)
                culture_score = interview_analysis_data.get('cultural_fit', {}).get('overall_score', 0)
                interview_score = (comm_score + tech_score + prob_score + culture_score) // 4
            
            # Calculate final score (60% interview, 40% resume)
            final_score = (interview_score * 0.6) + (resume_score * 0.4)
            
            return {
                'resume_score': resume_score,
                'interview_score': interview_score,
                'final_score': round(final_score, 2),
                'recommendation': self.get_recommendation(final_score),
                'grade': self.get_grade(final_score)
            }
        except Exception as e:
            print(f"Score calculation error: {e}")
            return {
                'resume_score': 0,
                'interview_score': 0,
                'final_score': 0,
                'recommendation': 'Error calculating scores',
                'grade': 'F'
            }
    
    def get_recommendation(self, score):
        if score >= 85:
            return "🚀 Strongly Recommended - Top Candidate"
        elif score >= 75:
            return "✅ Recommended - Good Fit"
        elif score >= 65:
            return "🤔 Consider - Potential Candidate"
        else:
            return "❌ Not Recommended - Poor Fit"
    
    def get_grade(self, score):
        if score >= 90: return 'A+'
        elif score >= 85: return 'A'
        elif score >= 80: return 'B+'
        elif score >= 75: return 'B'
        elif score >= 70: return 'C+'
        elif score >= 65: return 'C'
        elif score >= 60: return 'D'
        else: return 'F'