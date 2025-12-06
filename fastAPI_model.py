from fastapi import FastAPI
from pydantic import BaseModel
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

# Cargar modelo en CPU
model_path = "./Roberta_model"
tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModelForCausalLM.from_pretrained(model_path, is_decoder=True).to("cpu")  # Mover a CPU

# Inicializar FastAPI
app = FastAPI()

class PromptRequest(BaseModel):
    text: str
    max_length: int = 100

@app.post("/api/generate")
def generate_text(request: PromptRequest):
    inputs = tokenizer(request.text, return_tensors="pt").to("cpu")
    output = model.generate(**inputs, max_length=request.max_length)
    return {"response": tokenizer.decode(output[0], skip_special_tokens=True)}

# Para ejecutar el servidor: uvicorn fastAPI_model:app --host 0.0.0.0 --port 8000
