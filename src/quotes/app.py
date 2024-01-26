from fastapi import FastAPI
from app_container import AppContainer

app_container = AppContainer()


def create_app() -> FastAPI:
    app = FastAPI(title="Harvest Quotes", docs_url="/")

    hq_endpoint = app_container.hq_endpoint()

    app.include_router(hq_endpoint.router)

    app.container = app_container

    return app
