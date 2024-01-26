from mangum import Mangum
import uvicorn
from app import create_app

app = create_app()
mangum_handler = Mangum(app, lifespan="off")


@app.get("/healthcheck")
async def healthcheck():
    return {"status": "OK"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001, env_file='local.env')
