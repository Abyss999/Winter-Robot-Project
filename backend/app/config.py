from app.imports import *

load_dotenv()

class BaseConfig:
    SQLAlchemy_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get("SECRET_KEY", "CHANGE_ME")
    # frontend 
    FRONTEND_ORIGIN = os.environ.get("FRONTEND_ORIGIN", "http://localhost:5173")
    # jwt 
    JWT_SECRET_KEY = os.environ.get("JWT_SECRET_KEY", "CHANGE_ME")
    JWT_TOKEN_LOCATION = ["headers"],
    JWT_HEADER_NAME = "Authorization",
    JWT_HEADER_TYPE = "Bearer", 
    JWT_ACCESS_TOKEN_EXPIRES = 3600 # 1 hour 


class DevConfig(BaseConfig):
    DEBUG = True 
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL",
        "postgresql://dev_user:dev_pass@localhost:5432/dev_db"
    )

class TestConfig(BaseConfig):
    TESTING = True 
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL",
        "postgresql://test_user:test_pass@localhost:5432/test_db"
    )

