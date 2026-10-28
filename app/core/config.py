from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):

    # -- CORE SETTINGS --
    PROJECT_NAME: str = "Shope Ease"
    BACKEND_URL: str
    #-- DATABASE --
    DATABASE_URL: str

    # -- LOAD CONFIGURATION FROM ENV --
    model_config = SettingsConfigDict(
        env_file=".env", 
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore"
    )

settings = Settings()
