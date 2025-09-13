from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import psycopg2

app = FastAPI()

# CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Hello from backend!"}

@app.get("/db")
def check_db():
    try:
        conn = psycopg2.connect(
            host="db", user="postgres", password="postgres", dbname="testdb"
        )
        cur = conn.cursor()
        cur.execute("SELECT NOW();")
        result = cur.fetchone()
        return {"db_time": result[0]}
    except Exception as e:
        return {"error": str(e)}

