from os import getenv

PLATFORM = getenv("PLATFORM", "local")
SWAGGER_URL = getenv("SWAGGER_URL", "http://127.0.0.1:8000")
API_HOST = getenv("API_HOST", "127.0.0.1")
BOT_TOKEN = getenv("BOT_TOKEN", "")
CHAT_IDS = {
    "status": getenv("CHAT_ID_INFO", ""),
    "log": getenv("CHAT_ID_LOG", ""),
}

BACKEND_REDIS_HOST = getenv("BACKEND_REDIS_HOST", "127.0.0.1")
BACKEND_REDIS_PORT = getenv("BACKEND_REDIS_PORT", "6379")

BACKEND_POSTGRES_HOST = getenv("BACKEND_POSTGRES_HOST", "127.0.0.1")
BACKEND_POSTGRES_PORT = getenv("BACKEND_POSTGRES_PORT", "5432")
BACKEND_POSTGRES_NAME = getenv("BACKEND_POSTGRES_NAME", "postgres")
BACKEND_POSTGRES_USERNAME = getenv("BACKEND_POSTGRES_USERNAME", "postgres")
BACKEND_POSTGRES_PASSWORD = getenv("BACKEND_POSTGRES_PASSWORD", "postgres")

REDIS_DEFAULT = "0"
REDIS_RATELIMIT = "1"
REDIS_CELERY_BROKER = "2"
REDIS_CELERY_BACKEND = "3"
REDIS_CACHE_LOCK = "4"
REDIS_TRY_RATE = "5"
REDIS_ROUTINE_TIMING = "6"
