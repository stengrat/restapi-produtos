import environ

from api.settings.base import *

env = environ.Env()

DEBUG = env.bool("DEBUG",False)

SECRET_KEY = env("SECRET_KEY")

ALLOWED_HOSTS = env.list("ALLOWED_HOSTS")

DATABASES = {
    "default": env.db(),
}