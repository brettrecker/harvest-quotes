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
                                  summary="Root")

        self.router.add_api_route("/quotes",
                                  self.process_message,
                                  methods=["POST", "PATCH", "PUT", "GET"],
                                  summary="Quotes")

        self.router.add_api_route("/customers",
                                  self.process_message,
                                  methods=["POST", "PATCH", "PUT", "GET"],
                                  summary="Customers")

        self.router.add_api_route("/users",
                                  self.process_message,
                                  methods=["POST", "PATCH", "PUT", "GET"],
                                  summary="Users")

        self.router.add_api_route("/companies",
                                  self.process_message,
                                  methods=["POST", "PATCH", "PUT", "GET"],
                                  summary="Companies")

    async def process_message(self):
        return 'test'
