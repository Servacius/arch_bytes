from pydantic_settings import BaseSettings

class Config(BaseSettings):
    geminiai_api_key: str

    class Config:
        env_file = ".env"

settings = Config()