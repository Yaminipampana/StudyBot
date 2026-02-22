from fastapi import FastAPI
from pydantic import BaseModel
from langchain_groq import ChatGroq
from pymongo import MongoClient
from dotenv import load_dotenv
import os
from datetime import datetime

load_dotenv()

app = FastAPI(title="StudyBot")

# Load keys
groq_key = os.getenv("GROQ_API_KEY")
mongo_uri = os.getenv("MONGO_URI")

# LLM
llm = ChatGroq(
    groq_api_key=groq_key,
    model_name="llama-3.1-8b-instant"
)

# MongoDB
client = MongoClient(mongo_uri)
db = client["studybot"]
collection = db["chats"]

class ChatRequest(BaseModel):
    user_id: str
    query: str

@app.get("/")
def home():
    return {"message": "Study Bot Running"}

@app.post("/chat")
def chat(req: ChatRequest):

    try:
        # Get history
        history = collection.find({"user_id": req.user_id})

        context = ""
        for h in history:
            context += f"User: {h['query']}\nBot: {h['response']}\n"

        prompt = context + "User: " + req.query

        # Call Groq
        response = llm.invoke(prompt)

        bot_reply = response.content

        # Save to MongoDB
        collection.insert_one({
            "user_id": req.user_id,
            "query": req.query,
            "response": bot_reply,
            "time": datetime.utcnow()
        })

        return {"response": bot_reply}

    except Exception as e:

        return {"error": str(e)}
