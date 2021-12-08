# [HTM-Building stock screener with FastAPI](filepath)

## Create main app
- from documentation

main.py app
```python
from typing import Optional
from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}
```

## Run the server

```
uvicorn main:app --reload
```
### References
- [FastAPI](https://fastapi.tiangolo.com/)
- [asdf]()


