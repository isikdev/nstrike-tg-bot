from pydantic_settings import BaseSettings, SettingsConfigDict
from dotenv import load_dotenv
import os


load_dotenv()

class Settings(BaseSettings):
    BOT_TOKEN: str  
    URL:str

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
