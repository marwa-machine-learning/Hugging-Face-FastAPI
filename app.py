from fastapi import FastAPI
from pydantic import BaseModel
pipeline = 

app = FastAPI()

@app.get("/ping")
def index():
    return {"message": "pong"}

@app.post("/echo")
def echo(message: str):
    return {"message": message}
    
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)

def echo(message: str):
    return {"message": message}

def echo(message: str, name: str):
    return {"message": message, "name": name}

from pydantic import BaseModel

class TextToTranslate(BaseModel):
    input_text: str

def echo(text_to_translate: TextToTranslate):
    return {"message": text_to_translate.input_text}

{
  "input_text": "Hello World"
}
{
  "message": "Hello World"
}