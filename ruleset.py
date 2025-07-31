import re

def detect_threats(text):
    text = text.lower()  # normalize input

    threat_keywords = {
        "Phishing": [
            "login", "log in", "account suspended", "verify", "click here", 
            "update your payment", "password reset", "confirm your credentials",
            "security alert", "your bank account", "unfreeze"
        ],
        "Scam": [
            "congratulations", "you have won", "claim your prize", "lottery", 
            "send money", "urgent payment", "limited offer", "exclusive deal"
        ],
        "Abuse": [
            "hate you", "kill you", "worst person", "stupid", "shut up", 
            "you idiot", "dumb", "moron"
        ]
    }

    detected = {}

    for category, keywords in threat_keywords.items():
        matches = [kw for kw in keywords if re.search(rf"\b{re.escape(kw)}\b", text)]
        if matches:
            detected[category] = matches

    return detected