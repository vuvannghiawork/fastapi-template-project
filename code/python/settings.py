from loguru import logger
from environs import Env


log_file_format = "{time:YYYY-MM-DD}.log"
logger.add(f"logging/{log_file_format}", rotation="00:00", retention="7 days", enqueue=True)


env = Env()
logger.info(f"Loading environment variables...")


FASTAPI_ENVIRONMENT = env.str("FASTAPI_ENVIRONMENT", default="PRODUCTION")
SERVER_IP = env.str("SERVER_IP", default="0.0.0.0")
SERVER_PORT = env.int("SERVER_PORT", default=5000)
