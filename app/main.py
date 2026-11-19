"""Synthetic data only. Intentionally vulnerable application for a local lab."""
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from app.security import find_works

app = FastAPI(title="DevSecOps classroom lab")

@app.middleware("http")
async def security_headers(request, call_next):
    response = await call_next(request)
    response.headers["X-Frame-Options"] = "DENY"
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response

@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/", response_class=HTMLResponse)
def home():
    return """<!doctype html>
<html><head><title>Classroom works</title></head>
<body><h1>Classroom works</h1>
<p>Local security laboratory using synthetic data.</p>
<a href="/works?owner=Alice">Alice's works</a>
<a href="/works?owner=Bruno">Bruno's works</a>
<a href="/health">Health</a>
</body></html>"""


@app.get("/works")
def works(owner: str = "Alice"):
    return find_works(owner)
