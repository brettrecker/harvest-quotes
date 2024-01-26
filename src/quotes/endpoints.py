from fastapi import APIRouter


class HQEndpoints:

    def __init__(self):
        self.router = APIRouter()
        self.add_routes()

    def add_routes(self):
        """Define the routes that connect the http methods to the handler functions."""

        self.router.add_api_route("/",
                                  self.process_message,
                                  methods=["POST"],
                                  summary="Testing")

    async def process_message(self):
        return 'test'
