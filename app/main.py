from fastapi import FastAPI
from app.models import SecurityEvent
from app.analyzer import analyze_event
from app.logger import save_event

app = FastAPI()


@app.get("/")
def home():
    return {
        "message": "Security Automation API funcionando"
    }


@app.post("/events")
def receive_event(event: SecurityEvent):

    alerts = analyze_event(event)

    save_event(event, alerts)

    return {
        "message": "Evento recibido",
        "event": event,
        "alerts": alerts
    }