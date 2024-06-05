from fastapi import FastAPI
from dotenv import load_dotenv
from routes.category_routes import categories
from routes.question_routes import questions
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(categories)
app.include_router(questions)

load_dotenv()
