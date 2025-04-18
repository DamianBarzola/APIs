import os
from dotenv import load_dotenv

load_dotenv()

class DevConfig:
    def __init__(self):
        self.ENV = "development"
        self.DEBUG = True
        self.PORT = 8000
        self.HOST = '0.0.0.0'

class ProductionConfig:
    def __init__(self):
        self.ENV = "production"
        self.DEBUG = False
        self.PORT = 80
        self.HOST = '0.0.0.0'

class DBConnector:
    def __init__(self):
        self.SQLALCHEMY_DATABASE_URI  = os.getenv("POSTGRES_URL")
        self.SQLALCHEMY_TRACK_MODIFICATIONS = False


class Config:
    def __init__(self):
        self.dev_config = DevConfig()
        self.production_config = ProductionConfig()