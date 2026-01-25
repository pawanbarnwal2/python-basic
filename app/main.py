from fastapi import FastAPI
from fastapi.responses import JSONResponse
from app.database import Base, engine
from app.routes.user_routes import router
from app.exceptions import UserNotFound, InvalidUserData, DuplicateEmail

Base.metadata.create_all(bind=engine)

app = FastAPI(title="FastAPI MVC Example")

# Exception handlers
@app.exception_handler(UserNotFound)
async def user_not_found_handler(request, exc):
    return JSONResponse(
        status_code=404,
        content={"detail": "User not found"}
    )

@app.exception_handler(InvalidUserData)
async def invalid_user_data_handler(request, exc):
    return JSONResponse(
        status_code=400,
        content={"detail": str(exc)}
    )

@app.exception_handler(DuplicateEmail)
async def duplicate_email_handler(request, exc):
    return JSONResponse(
        status_code=409,
        content={"detail": "Email already exists"}
    )

app.include_router(router)

# app = FastAPI()

# @app.get("/")
# def root():
#     return {"message": "Hello FastAPI!"}


# @app.get("/{id}")
# def get_Product(id: int):
# 	return {
# 		"item":"1",
# 	    "itemName":"fast api examples"
# 	}




# @app.get("/search")
# def search_item(q: str = None):
#     return {"query": q}