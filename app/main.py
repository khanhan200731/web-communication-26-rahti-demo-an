from fastapi import FastAPI
from fastapi import Request
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/")
def read_root():
    return { "msg": "Hello an!", "v": "0.3" }


@app.get("/items/{id}")
def read_item(item_id: int, q: str = None):
    return {"id": id, "q": q}
app = FastAPI()


my_name= "an"
@app.get("/")
def read_root():
    local_var = "Hello"
    return {"msg": "Hello " +my_name}

@app.get("/api/ip")
def get_ip_json(request: Request):
    ip=request.client.host
    return {"ip" : ip}

@app.get("/ip", response_class=HTMLResponse)
def get_ip_html(request: Request):
    ip = request.client.host
    return f"<h1>Your public IP is {ip}</h1>"