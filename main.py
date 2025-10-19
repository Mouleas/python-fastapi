from fastapi import FastAPI

app = FastAPI()

items = [
    {"id": 1, "name": "Item One"},
    {"id": 2, "name": "Item Two"},
    {"id": 3, "name": "Item Three"},
]

@app.get("/healthy")
def check_healthy():
    return {
        "status": "OK",
        "message": "Your application is healthy!"
    }


@app.get("/")
def read_root():
    return {
        "status": "OK",
        "message": "Welcome to the FastAPI application!"
    }

@app.get("/items/")
def read_item():
    return {
        "status": "OK",
        "message": "List of items retrieved successfully.",
        "count": len(items),
        "data": items
    }


@app.post("/items/")
def create_item(item: dict):
    items.append(item)
    return {
        "status": "OK",
        "message": "Item created successfully.",
        "count": len(items),
        "data": item
    }

@app.get("/items/{item_id}")
def read_item_by_id(item_id: int):
    for item in items:
        if item["id"] == item_id:
            return {
                "status": "OK",
                "message": "Item retrieved successfully.",
                "data": item
            }
    return {
        "status": "Error",
        "message": "Item not found."
    }


