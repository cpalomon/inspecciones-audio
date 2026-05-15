from fastapi import FastAPI, UploadFile, File
from fastapi.responses import HTMLResponse
import os
from datetime import datetime

app = FastAPI()

# ✅ Ruta principal
@app.get("/", response_class=HTMLResponse)
def home():
    return open("grabador.html").read()


# ✅ Endpoint para guardar audio
@app.post("/upload")
async def upload_audio(file: UploadFile = File(...)):

    # Crear carpeta si no existe
    os.makedirs("audios", exist_ok=True)

    # Nombre único
    filename = f"{datetime.now().strftime('%Y%m%d_%H%M%S')}.webm"
    filepath = f"audios/{filename}"

    # Guardar archivo
    with open(filepath, "wb") as buffer:
        buffer.write(await file.read())

    print(f"✅ Audio guardado: {filepath}")

    return {"message": "ok", "file": filename}