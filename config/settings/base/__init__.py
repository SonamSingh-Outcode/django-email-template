from ._base import *
from .apps import *
from .cors import *
from .database import *
from .email import *
from .logger import *
from .rest_framework import *
from .simple_jwt import *
from .swagger import *

if os.path.exists('.env') is False:
    raise ImportError(
        "\n***********************************************\n"
        "Couldn't import the environment file for APP \n"
        "Env file should exists in root project directory\n"
        "You should create a `.env` file first in the root directory of a project\n"
        "***********************************************\n")
elif len(SECRET_KEY) < 32:
    raise SystemError('SECRET_KEY must be greater or equals to 32 characters.')