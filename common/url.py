from dataclasses import dataclass
from typing import Callable


@dataclass
class Url:
    path: str
    view: Callable



