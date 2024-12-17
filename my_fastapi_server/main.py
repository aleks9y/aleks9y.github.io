from fastapi import FastAPI, File, UploadFile, Form
from fastapi.responses import JSONResponse
from typing import List
import os

# Создаем экземпляр приложения
app = FastAPI()

# Директория для сохранения файлов
UPLOAD_DIRECTORY = "uploads/"
os.makedirs(UPLOAD_DIRECTORY, exist_ok=True)

@app.post("/upload/")
async def upload_data(
    name: str = Form(...),
    about: str = Form(...),
    files: List[UploadFile] = File(...)
):
    """
    Обработка данных пользователя и загрузка файлов.
    """
    # Сохраняем файлы на сервер
    saved_files = []
    for file in files:
        file_path = os.path.join(UPLOAD_DIRECTORY, file.filename)
        with open(file_path, "wb") as f:
            f.write(await file.read())
        saved_files.append(file_path)

    # Ответ для клиента
    response_data = {
        "userInfo": {
            "name": name,
            "about": about,
        },
        "files": saved_files,
    }

    return JSONResponse(content=response_data)

