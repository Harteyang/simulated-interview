from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
import random
import openai
import json

app = FastAPI()

with open("questions.json", "r") as f:
    questions = json.load(f)

class Prompt(BaseModel):
    prompt: str

openai.api_key = "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"

def generate_question():
    topic = random.choice(list(questions.keys()))
    question = random.choice(questions[topic])
    return question

@app.get("/")
async def get_main_page():
    with open("templates/index.html", "r") as f:
        html_content = f.read()
    return HTMLResponse(content=html_content, status_code=200)

@app.get("/report")
async def get_report_page():
    with open("templates/report.html", "r") as f:
        html_content = f.read()
    return HTMLResponse(content=html_content, status_code=200)

@app.post("/start-interview")
async def start_interview(prompt: Prompt):
    question = generate_question()
    return {"question": question}

@app.post("/next-question")
async def next_question(prompt: Prompt):
    question = generate_question()
    return {"question": question}

@app.post("/generate-report")
async def generate_report():
    report = "这里是一份模拟的面试报告。"
    return {"report": report}
