import psutil
import shutil

def get_snapshot():
    return {
        "cpu_percent": psutil.cpu_percent(interval=1),
        "memory": psutil.virtual_memory().used,
        "disk": shutil.disk_usage("/").used,
        "processes": [p.info for p in psutil.process_iter(['pid', 'name', 'cpu_percent'])]
    }