from fastapi import FastAPI, File, Form, UploadFile
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import os

app = FastAPI()

# Разрешаем CORS для доступа с вашего веб-приложения
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Папка для сохранения файлов
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.post("/upload")
async def upload_data(
    name: str = Form(...),
    about: str = Form(...),
    files: list[UploadFile] = File(...),
):
    saved_files = []
    for file in files:
        file_path = os.path.join(UPLOAD_FOLDER, file.filename)
        with open(file_path, "wb") as f:
            f.write(await file.read())
        saved_files.append(file_path)

    return JSONResponse(content={
        "status": "success",
        "message": f"Файлы успешно загружены: {len(saved_files)}",
        "files": saved_files,
        "user_info": {"name": name, "about": about}
    })
