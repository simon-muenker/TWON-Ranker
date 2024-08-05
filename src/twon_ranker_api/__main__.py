import uvicorn

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import twon_ranker
import twon_ranker_api.config

cfg = twon_ranker_api.Config()

ranker = twon_ranker.Ranker(log_path=cfg.log_path)

app = FastAPI(
    title=cfg.title,
    description=open(f"{cfg.docs_path}/index.md").read(),
    version=cfg.version,
    docs_url="/",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=cfg.trust_origins,
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/rank/", summary="todo", description=open(f"{cfg.docs_path}/rank.md").read())
async def rank(req: twon_ranker.Request) -> twon_ranker.Response:
    return ranker(req)


if __name__ == "__main__":
    uvicorn.run(app)