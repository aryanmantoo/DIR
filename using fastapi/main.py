from fastapi import FastAPI
import converter
from converter import File

app = FastAPI()

@app.post("/convert_json")
async def convert_json(input_files: list = converter.File(...), output_files: list = converter.File(...)):
    return await converter.convert_files(input_files, output_files)
