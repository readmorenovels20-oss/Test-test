import os
import asyncio
from fastapi import FastAPI
import uvicorn
from pyrogram import Client
from config import API_ID, API_HASH, BOT_TOKEN

# Initialize FastAPI app for Render Web Service port binding
app_fastapi = FastAPI()

@app_fastapi.get("/")
async def root():
    return {"status": "Story Adda Bot is active and running!"}

# Initialize Kurigram Client
app_pyrogram = Client(
    "StoryAddaBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="handlers")
)

@app_fastapi.on_event("startup")
async def startup_event():
    # Start Pyrogram bot in background task so FastAPI can bind to the port
    asyncio.create_task(app_pyrogram.start())
    print("🚀 Kurigram Bot started successfully!")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    uvicorn.run(app_fastapi, host="0.0.0.0", port=port)
