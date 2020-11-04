import uvicorn

import config
from core.service import app

if __name__ == "__main__":
    uvicorn.run(app, host=config.HOST, port=config.PORT)
