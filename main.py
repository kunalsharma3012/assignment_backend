from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional, List, Dict, Any

from db import get_connection

app = FastAPI()

# allow your frontend to call this API
origins = [
    "http://localhost:3000",            # local Next.js dev
    "https://your-frontend.vercel.app", # change after deploy
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/campaigns")
def get_campaigns(status: Optional[str] = Query(default=None)):
    """
    GET /campaigns
    Optional query param: ?status=Active or ?status=Paused
    Returns: list of campaign dicts.
    """
    conn = get_connection()
    cursor = conn.cursor()

    if status in ("Active", "Paused"):
        cursor.execute("SELECT * FROM campaigns WHERE status = ?", (status,))
    else:
        cursor.execute("SELECT * FROM campaigns")

    rows = cursor.fetchall()
    conn.close()

    # convert sqlite Row -> dict
    campaigns: List[Dict[str, Any]] = [dict(row) for row in rows]
    return campaigns
