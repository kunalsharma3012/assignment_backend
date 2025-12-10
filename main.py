from typing import Optional, List, Dict, Any

from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware

from db import get_connection 

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],         
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {"message": "Backend is running"}


@app.get("/campaigns")
def get_campaigns(status: Optional[str] = Query(default=None)):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        if status in ("Active", "Paused"):
            cursor.execute("SELECT * FROM campaigns WHERE status = ?", (status,))
        else:
            cursor.execute("SELECT * FROM campaigns")

        rows = cursor.fetchall()
        campaigns: List[Dict[str, Any]] = [dict(row) for row in rows]
        return campaigns
    finally:
        conn.close()
