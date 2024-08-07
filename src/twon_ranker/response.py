import datetime
import json
import typing
import uuid

import pydantic

from twon_ranker.request import Request


class Response(pydantic.BaseModel):
    id: uuid.UUID = None
    timestamp: datetime.datetime = None

    request: Request
    ranking_map: typing.Dict[str, float]

    def __init__(self, log_path: str = None, **data):
        super().__init__(**data)

        self.id = uuid.uuid1()
        self.timestamp = datetime.datetime.now()

        if log_path:
            self.log(log_path)

    def log(self, path: str) -> None:
        json.dump(
            self.model_dump(mode="json", exclude=set("log_path")),
            open(f"{path}/{self.id}.json", "w"),
            indent=4,
        )
