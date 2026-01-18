from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello FastAPI!"}


# @app.get("/{id}")
# def get_Product(id: int):
# 	return {
# 		"item":"1",
# 	    "itemName":"fast api examples"
# 	}




@app.get("/search")
def search_item(q: str = None):
    return {"query": q}