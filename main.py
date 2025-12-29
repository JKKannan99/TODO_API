from fastapi import FastAPI

from routes.Todo_routes import Todo_route

app = FastAPI()

app.include_router(Todo_route)