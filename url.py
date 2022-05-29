from framework.view import View


@dataclass
class Url:

    path: str
    view: View
