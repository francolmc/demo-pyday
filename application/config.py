import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_CONNECTION_STRING")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_TEST_CONNECTION_STRING", "sqlite:///:memory:")