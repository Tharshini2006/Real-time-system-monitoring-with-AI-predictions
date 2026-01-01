from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import psutil

from predict import predict_cpu

app = FastAPI(title="Real-Time System Monitoring with AI")

# Allow frontend (Live Server / browser) to access API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {"message": "System Monitoring API is running"}


@app.get("/status")
def get_system_status():
    cpu_usage = psutil.cpu_percent(interval=1)
    ram_usage = psutil.virtual_memory().percent
    disk_usage = psutil.disk_usage("/").percent

    predicted_cpu = predict_cpu(ram_usage, disk_usage)

    return {
        "cpu_usage": cpu_usage,
        "ram_usage": ram_usage,
        "disk_usage": disk_usage,
        "predicted_cpu_usage": round(predicted_cpu, 2)
    }
