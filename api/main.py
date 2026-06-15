from pathlib import Path

from fastapi import FastAPI

from api.routes.answer import router_answer
import logging
logFolder: Path = Path(__file__ ).parents[1] / "logs"
logFolder.mkdir(parents=True, exist_ok=True)
logging.basicConfig(filename=logFolder / "answer_agent.log", filemode="w", level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

app = FastAPI()
app.include_router(router_answer)