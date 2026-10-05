failed_attempts = {}


def analyze_event(event):
    alerts = []

    if event.action == "login" and event.success is False:

        ip = event.ip

        if ip not in failed_attempts:
            failed_attempts[ip] = 0

        failed_attempts[ip] += 1

        if failed_attempts[ip] >= 5:
            alerts.append(
                "Posible ataque de fuerza bruta detectado"
            )

    return alerts