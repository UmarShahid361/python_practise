from fastapi import FastAPI, HTTPException, BaseModel

app = FastAPI()


class LoginData(BaseModel):
    username: str
    password: str


@app.post("/login")
def login(data: LoginData):
    return {
        "message": "Welcome",
        "user": data.username,
    }


@app.get("/items/{items_id}")
def get_items(items_id: int, verbose: bool = False):
    if items_id < 0:
        raise HTTPException(status_code=400, detail="Negative IDs not allowed")
    else:
        return {
            "items_id": items_id,
            "verbose": verbose,
        }
