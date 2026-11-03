import os
import socket
import uvicorn

def find_free_port(start_port=8080):
    port = start_port
    while port < 65535:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            try:
                s.bind(("0.0.0.0", port))
                return port
            except OSError:
                port += 1
    return start_port

if __name__ == "__main__":
    free_port = find_free_port(8080)
    print(f"🔥 [ABYSSAL-CORE] Iniciando servidor en puerto dinámico seguro: {free_port}")
    uvicorn.run("server:app", host="0.0.0.0", port=free_port, workers=1, log_level="info")
