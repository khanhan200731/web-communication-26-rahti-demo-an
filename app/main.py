from fastapi import FastAPI
from fastapi import Request

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