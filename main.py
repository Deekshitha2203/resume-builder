import os
from openai import OpenAI
from dotenv import load_dotenv
import gradio as g

load_dotenv()
user = OpenAI(api_key=os.environ['token'])
model = os.environ['model']

def resume_builder(resume, jd):
    prompt = f'''You are the Hiring Manager of the company for which the Job Description is provided. Using the provided resume and without changing the content's meaning just make the resume really effective by enhancing the way the content is put matiching to the job description.
    Use STAR method; for each experience or project give no more than 3 points; keep the points effective use did X which lead to Y - like that format to enhance the effectiveness. Also alter the skills section accordingly but dont add new skills just to suffice the job description. only add if the person has it or proves to have it based on their entire resume.
    This is the resume: {resume}
    This is the Job Description: {jd}
    Give the tailored resume only and in a completely formated way.'''
    response = user.chat.completions.create(model=model, messages=[{"role": "user", "content": prompt}])
    return response.choices[0].message.content

hf = g.Interface(fn=resume_builder, inputs=[g.Textbox(placeholder="Resume", label="Resume"), g.Textbox(placeholder="Job Description", label="Job Description")], outputs=g.Markdown(), flagging_mode="never")
hf.launch(server_name="0.0.0.0", server_port=7860) 
