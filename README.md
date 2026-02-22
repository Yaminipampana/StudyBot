# Study Bot Chatbot Project

## Project Overview
Study Bot is an AI-powered chatbot that helps students by answering academic questions. It uses Groq LLM to generate responses and MongoDB to store chat history. The chatbot is built using FastAPI and deployed on Render.

## Objectives
- Build chatbot using LLM
- Implement memory using MongoDB
- Create FastAPI backend
- Deploy chatbot online

## Technologies Used
- Python
- FastAPI
- MongoDB Atlas
- Groq API
- Render
- GitHub

## System Architecture
User → FastAPI → Groq LLM → MongoDB → Response

## Memory Implementation
The chatbot stores user conversations in MongoDB using user_id. When a new query is asked, previous chats are retrieved and added to the prompt to provide context-aware responses.

## API Endpoint

POST /chat

- Example Request:{"user_id": "student1","query": "What is AI?"}


- Example Response: {"response": "Artificial Intelligence is..."}


## Deployment Link
https://studybot-qq9t.onrender.com

## GitHub Repository Link
https://github.com/Yaminipampana/StudyBot

## Conclusion
The Study Bot chatbot was successfully developed using FastAPI, MongoDB, and Groq API. It provides intelligent academic assistance and supports conversational memory.
