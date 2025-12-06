# Bert Model API

Este proyecto implementa una API REST simple utilizando **FastAPI** para servir un modelo de lenguaje basado en **RoBERTa** de manera local.

## 📋 Descripción

El servidor carga un modelo pre-entrenado desde la carpeta local `./Roberta_model` y lo ejecuta en la **CPU**. Expone un endpoint para generar texto a partir de un prompt.

### Características
- **Framework**: FastAPI (Python).
- **Modelo**: RoBERTa (Causal Language Model).
- **Ejecución**: CPU (optimizado para entornos sin GPU dedicada).

## 🚀 Instalación y Uso

### Prerrequisitos
- Python 3.8+
- PyTorch
- Transformers
- FastAPI
- Uvicorn

### Instalación de dependencias
```bash
pip install fastapi uvicorn torch transformers
```

### Ejecutar el servidor
Navega a la carpeta del proyecto y ejecuta:

```bash
uvicorn fastAPI_model:app --host 0.0.0.0 --port 8000
```

El servidor iniciará en `http://localhost:8000`.

## 🔌 Uso de la API

### Endpoint: `POST /api/generate`

Genera texto basado en una entrada.

**Cuerpo de la petición (JSON):**
```json
{
  "text": "El aprendizaje automático es",
  "max_length": 50
}
```

**Respuesta:**
```json
{
  "response": "El aprendizaje automático es una rama de la inteligencia artificial..."
}
```

## 📂 Estructura del Proyecto

- `fastAPI_model.py`: Script principal que define la API y carga el modelo.
- `Roberta_model/`: Carpeta que contiene los pesos y configuración del modelo (formato Hugging Face).
