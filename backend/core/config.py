from dotenv import load_dotenv
import os
from pydantic_settings import BaseSettings

# Загрузка переменных окружения из .env файла
load_dotenv()

# Проверка наличия переменной окружения для отладки
CMC_API_KEY = os.getenv("CMC_API_KEY")

if CMC_API_KEY is None:
    raise ValueError("Переменная окружения CMC_API_KEY не установлена")
print(f"CMC_API_KEY: {CMC_API_KEY}")

class Settings(BaseSettings):
    CMC_API_KEY: str

    class Config:
       env_file = ".env"

# Создание экземпляра настроек
settings = Settings()