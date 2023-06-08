from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse, StreamingResponse
from typing import Annotated
from fastapi.middleware.cors import CORSMiddleware

# from PIL import Image
import io
from testmodel import predict_image_from_file

app = FastAPI()

# allow the front end to communicate with the backend
origins = ["http://localhost:8000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/")
async def main(file: UploadFile = File(...)):
    # Read the file contents as bytes
    image_contents = await file.read()
    category = predict_image_from_file(image_contents)
    return {"category": category}
