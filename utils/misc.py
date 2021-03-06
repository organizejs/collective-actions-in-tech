import datetime
import ast
import os
from pathlib import Path
from typing import Any


Url = str
NoneType = type(None)


ACTION_FOLDER = Path(
    os.path.realpath(
        os.path.join(
            os.path.abspath(__file__), os.pardir, os.pardir, "actions"
        )
    )
)


README = Path(
    os.path.realpath(
        os.path.join(
            os.path.abspath(__file__), os.pardir, os.pardir, "README.md"
        )
    )
)


CSV = Path(
    os.path.realpath(
        os.path.join(
            os.path.abspath(__file__), os.pardir, os.pardir, "actions.csv"
        )
    )
)


JSON = Path(
    os.path.realpath(
        os.path.join(
            os.path.abspath(__file__), os.pardir, os.pardir, "actions.json"
        )
    )
)


CSV_FLAG = Path(
    os.path.realpath(
        os.path.join(
            os.path.abspath(__file__), os.pardir, os.pardir, "CSV_FLAG"
        )
    )
)


def ca_json_converter(o: Any) -> str:
    """ converts datetime to str if type is datetime """
    if isinstance(o, datetime.date):
        return o.strftime("%Y/%m/%d")


def literal_eval(val) -> Any:
    """ Converts a string literal to python object. """
    try:
        return ast.literal_eval(val)
    except (SyntaxError, ValueError):
        return val
