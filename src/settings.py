from pydantic import BaseSettings


class Settings(BaseSettings):
    API_TOKEN: str
    CHAT_ID: int

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'


settings = Settings()
