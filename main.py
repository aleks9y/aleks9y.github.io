from fastapi import FastAPI, Form, File, UploadFile, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import os
from pathlib import Path

app = FastAPI()

# Папка для сохранения загруженных файлов
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Настройка шаблонов и статики
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def get_form(request: Request):
    return templates.TemplateResponse("form.html", {"request": request})

@app.post("/submit", response_class=HTMLResponse)
async def submit_form(
    request: Request,
    name: str = Form(...),
    about: str = Form(...),
    files: list[UploadFile] = File(...)
):
    # Сохраняем файлы
    saved_files = []
    for file in files:
        file_location = Path(UPLOAD_FOLDER) / file.filename
        with open(file_location, "wb") as f:
            f.write(await file.read())
        saved_files.append(file.filename)

    return templates.TemplateResponse(
        "success.html",
        {"request": request, "name": name, "about": about, "files": saved_files},
    )

# Создаем статические файлы и шаблоны
os.makedirs("static", exist_ok=True)
os.makedirs("templates", exist_ok=True)

# Сохранение CSS
with open("static/style.css", "w", encoding="utf-8") as f:
    f.write("""
        body {
            font-family: Arial, sans-serif;
            background-color: #f0f8ff;
            color: #333;
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }
        .container {
            background: #ffffff;
            border-radius: 10px;
            padding: 20px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            width: 400px;
            text-align: center;
        }
        input, textarea {
            width: 100%;
            padding: 10px;
            margin: 10px 0;
            border: 1px solid #ccc;
            border-radius: 5px;
        }
        button {
            background-color: #1e90ff;
            color: #fff;
            border: none;
            padding: 10px 20px;
            cursor: pointer;
            border-radius: 5px;
        }
        button:hover {
            background-color: #1c86ee;
        }
    """)

# Сохранение HTML-шаблонов
with open("templates/form.html", "w", encoding="utf-8") as f:
    f.write("""
        <!DOCTYPE html>
        <html>
        <head>
            <link rel="stylesheet" type="text/css" href="/static/style.css">
            <title>Форма</title>
        </head>
        <body>
            <div class="container">
                <h1>Отправьте свои данные</h1>
                <form action="/submit" method="post" enctype="multipart/form-data">
                    <input type="text" name="name" placeholder="Ваше имя" required>
                    <textarea name="about" placeholder="О себе" rows="5" required></textarea>
                    <input type="file" name="files" multiple required>
                    <button type="submit">Отправить</button>
                </form>
            </div>
        </body>
        </html>
    """)

with open("templates/success.html", "w", encoding="utf-8") as f:
    f.write("""
        <!DOCTYPE html>
        <html>
        <head>
            <link rel="stylesheet" type="text/css" href="/static/style.css">
            <title>Успех</title>
        </head>
        <body>
            <div class="container">
                <h1>Данные успешно отправлены!</h1>
                <p><strong>Имя:</strong> {{ name }}</p>
                <p><strong>О себе:</strong> {{ about }}</p>
                <p><strong>Загруженные файлы:</strong></p>
                <ul>
                    {% for file in files %}
                        <li>{{ file }}</li>
                    {% endfor %}
                </ul>
                <a href="/">Вернуться на главную</a>
            </div>
        </body>
        </html>
    """)
