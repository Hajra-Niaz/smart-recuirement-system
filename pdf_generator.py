# import os
# import datetime
# from xhtml2pdf import pisa
# from io import BytesIO

# class PDFGenerator:
#     @staticmethod
#     def generate_results_pdf(resume_analysis, interview_analysis, final_result, candidate_name="Candidate"):
#         try:
#             # Create HTML content for PDF
#             html_content = PDFGenerator._create_html_content(resume_analysis, interview_analysis, final_result, candidate_name)
            
#             # Generate PDF
#             pdf_dir = 'static/downloads'
#             os.makedirs(pdf_dir, exist_ok=True)
            
#             pdf_filename = f"candidate_report_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
#             pdf_path = os.path.join(pdf_dir, pdf_filename)
            
#             # Create PDF file using xhtml2pdf
#             with open(pdf_path, "w+b") as pdf_file:
#                 pisa_status = pisa.CreatePDF(
#                     html_content,
#                     dest=pdf_file,
#                     encoding='utf-8'
#                 )
            
#             if pisa_status.err:
#                 print("PDF generation error with xhtml2pdf")
#                 return None
                
#             return pdf_filename
            
#         except Exception as e:
#             print(f"PDF generation error: {e}")
#             # Return a dummy filename for testing
#             return f"candidate_report_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"

#     @staticmethod
#     def _create_html_content(resume_analysis, interview_analysis, final_result, candidate_name):
#         """Create HTML content for the PDF report"""
        
#         # Safely get values with fallbacks
#         resume_analysis_data = resume_analysis.get('analysis', {})
#         interview_analysis_data = interview_analysis.get('analysis', {})
        
#         skills_match = resume_analysis_data.get('skills_match', {})
#         experience_analysis = resume_analysis_data.get('experience_analysis', {})
        
#         communication_skills = interview_analysis_data.get('communication_skills', {})
#         technical_knowledge = interview_analysis_data.get('technical_knowledge', {})
#         problem_solving = interview_analysis_data.get('problem_solving', {})
#         cultural_fit = interview_analysis_data.get('cultural_fit', {})
        
#         # Get lists with fallbacks
#         matched_skills = skills_match.get('matched_skills', ['No skills analyzed'])
#         missing_skills = skills_match.get('missing_skills', ['No missing skills identified'])
#         resume_strengths = resume_analysis_data.get('strengths', ['No strengths identified'])
#         resume_recommendations = resume_analysis_data.get('recommendations', ['No recommendations'])
#         interview_strengths = interview_analysis_data.get('strengths', ['No strengths identified'])
#         interview_recommendations = interview_analysis_data.get('recommendations', ['No recommendations'])
        
#         return f"""
#         <!DOCTYPE html>
#         <html>
#         <head>
#             <meta charset="UTF-8">
#             <title>Candidate Evaluation Report</title>
#             <style>
#                 body {{ 
#                     font-family: Arial, sans-serif; 
#                     margin: 40px; 
#                     line-height: 1.6;
#                     color: #333;
#                 }}
#                 .header {{ 
#                     text-align: center; 
#                     border-bottom: 2px solid #333; 
#                     padding-bottom: 20px; 
#                     margin-bottom: 30px;
#                 }}
#                 .score-card {{ 
#                     background: #f8f9fa; 
#                     padding: 20px; 
#                     margin: 20px 0; 
#                     border-radius: 10px;
#                     text-align: center;
#                 }}
#                 .section {{ 
#                     margin: 30px 0; 
#                     padding: 15px;
#                     border-left: 4px solid #007bff;
#                     background: #f8f9fa;
#                 }}
#                 table {{ 
#                     width: 100%; 
#                     border-collapse: collapse; 
#                     margin: 20px 0; 
#                 }}
#                 th, td {{ 
#                     border: 1px solid #ddd; 
#                     padding: 12px; 
#                     text-align: left; 
#                 }}
#                 th {{ 
#                     background-color: #007bff;
#                     color: white;
#                 }}
#                 .final-score {{ 
#                     font-size: 36px; 
#                     font-weight: bold; 
#                     margin: 10px 0;
#                     color: #007bff;
#                 }}
#                 .badge {{
#                     background: #007bff;
#                     color: white;
#                     padding: 5px 10px;
#                     border-radius: 15px;
#                     margin: 2px;
#                     display: inline-block;
#                     font-size: 12px;
#                 }}
#                 .footer {{ 
#                     text-align: center; 
#                     margin-top: 40px; 
#                     padding-top: 20px;
#                     border-top: 1px solid #ddd;
#                     color: #666;
#                 }}
#             </style>
#         </head>
#         <body>
#             <div class="header">
#                 <h1>Smart Recruitment System</h1>
#                 <h2>Candidate Evaluation Report</h2>
#                 <p><strong>Generated on:</strong> {datetime.datetime.now().strftime("%Y-%m-%d %H:%M")}</p>
#                 <p><strong>Candidate:</strong> {candidate_name}</p>
#             </div>

#             <!-- Final Scores -->
#             <div class="score-card">
#                 <h2>Overall Evaluation</h2>
#                 <div class="final-score">{final_result['final_score']}/100</div>
#                 <p><strong>Grade:</strong> {final_result.get('grade', 'N/A')}</p>
#                 <p><strong>Recommendation:</strong> {final_result['recommendation']}</p>
#             </div>

#             <!-- Score Breakdown -->
#             <table>
#                 <tr>
#                     <th>Evaluation Component</th>
#                     <th>Score</th>
#                     <th>Weight</th>
#                 </tr>
#                 <tr>
#                     <td>Resume Analysis</td>
#                     <td>{final_result['resume_score']}/100</td>
#                     <td>40%</td>
#                 </tr>
#                 <tr>
#                     <td>Interview Analysis</td>
#                     <td>{final_result['interview_score']}/100</td>
#                     <td>60%</td>
#                 </tr>
#             </table>

#             <!-- Resume Analysis -->
#             <div class="section">
#                 <h2>Resume Analysis</h2>
                
#                 <p><strong>Skills Match:</strong> {skills_match.get('match_percentage', 0)}%</p>
                
#                 <p><strong>Matched Skills:</strong></p>
#                 <div>
#                     {' '.join([f'<span class="badge">{skill}</span>' for skill in matched_skills])}
#                 </div>
                
#                 <p><strong>Missing Skills:</strong></p>
#                 <div>
#                     {' '.join([f'<span class="badge" style="background: #dc3545;">{skill}</span>' for skill in missing_skills])}
#                 </div>
                
#                 <p><strong>Experience Level:</strong> {experience_analysis.get('experience_level', 'Not specified')}</p>
                
#                 <p><strong>Strengths:</strong></p>
#                 <ul>
#                     {''.join([f'<li>{strength}</li>' for strength in resume_strengths])}
#                 </ul>
                
#                 <p><strong>Recommendations:</strong></p>
#                 <ul>
#                     {''.join([f'<li>{rec}</li>' for rec in resume_recommendations])}
#                 </ul>
#             </div>

#             <!-- Interview Analysis -->
#             <div class="section">
#                 <h2>Interview Analysis</h2>
                
#                 <table>
#                     <tr>
#                         <th>Category</th>
#                         <th>Score</th>
#                     </tr>
#                     <tr>
#                         <td>Communication Skills</td>
#                         <td>{communication_skills.get('overall_score', 0)}/100</td>
#                     </tr>
#                     <tr>
#                         <td>Technical Knowledge</td>
#                         <td>{technical_knowledge.get('overall_score', 0)}/100</td>
#                     </tr>
#                     <tr>
#                         <td>Problem Solving</td>
#                         <td>{problem_solving.get('overall_score', 0)}/100</td>
#                     </tr>
#                     <tr>
#                         <td>Cultural Fit</td>
#                         <td>{cultural_fit.get('overall_score', 0)}/100</td>
#                     </tr>
#                 </table>

#                 <p><strong>Interview Strengths:</strong></p>
#                 <ul>
#                     {''.join([f'<li>{strength}</li>' for strength in interview_strengths])}
#                 </ul>
                
#                 <p><strong>Interview Recommendations:</strong></p>
#                 <ul>
#                     {''.join([f'<li>{rec}</li>' for rec in interview_recommendations])}
#                 </ul>
#             </div>

#             <div class="footer">
#                 <p>Generated by Smart Recruitment System</p>
#                 <p>Confidential Report - For Internal Use Only</p>
#             </div>
#         </body>
#         </html>
#         """