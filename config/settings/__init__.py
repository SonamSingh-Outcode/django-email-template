from .base import *

if os.path.exists('.env') is False:
    raise ImportError(
        "\n***********************************************\n"
        "Couldn't import the environment file for APP \n"
        "Env file should exists in root project directory\n"
        "You should create a `.env` file first in the root directory of a project\n"
        "***********************************************\n")
