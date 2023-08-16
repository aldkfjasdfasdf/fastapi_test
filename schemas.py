from typing import Any
from pydantic import BaseModel, Field


class DynamicList(BaseModel):
    arr: Any = Field(
        ...,
        title="Sort time",
        example=[
            'test',
            'word',
            8524,
            596,
            9375,
            7268,
            1850,
            1056,
            1995,
            9291,
            6431,
            2367,
            1308,
            7600,
            9548,
            2939,
            5653,
            7706,
            7521,
            2975,
            1390,
            6784,
        ],
    )
