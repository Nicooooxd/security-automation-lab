import json
from datetime import datetime


def save_event(event, alerts):
    log_entry = {
        "timestamp": datetime.now().isoformat(),
        "username": event.username,
        "ip": event.ip,
        "action": event.action,
        "success": event.success,
        "alerts": alerts
    }

    with open("data/events.log", "a", encoding="utf-8") as file:
        file.write(json.dumps(log_entry) + "\n")