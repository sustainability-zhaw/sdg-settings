import os

from sdg_settings import Settings

def settings_path(filename):
    return f"tests/data/{filename}"

def create_default_settings():
    return Settings({
        "PROJECT_DB_API_KEY": os.getenv("PROJECT_DB_API_KEY", ""),
        "DB_HOST": os.getenv("DB_HOST", "localhost:8080"),
        "IMPORT_INTERVAL": int(os.getenv('IMPORT_INTERVAL', 86400)), # 24h
        "BATCH_INTERVAL": int(os.getenv('BATCH_INTERVAL', 300)), # 5 min
        "BATCH_SIZE": int(os.getenv("BATCH_SIZE", 100)),
        "LOG_LEVEL": os.getenv("LOG_LEVEL", "ERROR"),
        "MQ_HOST": os.getenv("MQ_HOST", "mq"),
        "MQ_EXCHANGE": os.getenv("MQ_EXCHANGE", "zhaw-km"),
        "MQ_HEARTBEAT": int(os.getenv("MQ_HEARTBEAT", 6000)),
        "MQ_TIMEOUT": int(os.getenv("MQ_TIMEOUT", 3600)),
        "MQ_USER": os.getenv("MQ_USER", "extraction-projects"),
        "MQ_PASS": os.getenv("MQ_PASS", "guest")
    })
