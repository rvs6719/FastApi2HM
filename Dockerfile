# Dockerfile

# Используем официальный образ Python в качестве базового образа
FROM python:3.12-slim

# Устанавливаем рабочую директорию в контейнере
WORKDIR /app

# Копируем файлы requirements.txt и models.py в контейнер
COPY requirements.txt .
COPY backend/models.py .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем остальные файлы приложения в контейнер
COPY backend/ .

# Указываем команду для запуска приложения
CMD ["uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "8000"]