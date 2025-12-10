from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional, List, Dict, Any

from db import get_connection

app = FastAPI()


origin=["https://assignment-frontend-lilac.vercel.app"],

app.add_middleware(
    CORSMiddleware,
    allow_origins=origin, 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/campaigns")
def get_campaigns(status: Optional[str] = Query(default=None)):
    conn = get_connection()
    cursor = conn.cursor()

    if status in ("Active", "Paused"):
        cursor.execute("SELECT * FROM campaigns WHERE status = ?", (status,))
    else:
        cursor.execute("SELECT * FROM campaigns")

    rows = cursor.fetchall()
    conn.close()

    campaigns: List[Dict[str, Any]] = [dict(row) for row in rows]
    return campaigns
