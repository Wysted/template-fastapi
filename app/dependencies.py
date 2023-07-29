# Redis
import redis.asyncio as redis
# Fastapi
import fastapi
import fastapi.openapi.utils as openapi
import fastapi.responses as responses

status = fastapi.status
# Typing
import typing
# Pydantic
import pydantic
import pydantic.generics as generics
# Starlette
import starlette.exceptions as exceptions
from starlette_context import context, plugins
from starlette_context.middleware import RawContextMiddleware
# RaseLimiter
import fastapi_limiter as limiter
# CORS
import fastapi.middleware.cors as cors
# Mongo
from pymongo import mongo_client
import pymongo
# Interfaces
from app.interfaces.user_types import UserTypes
from app.interfaces.res import Res
from app.interfaces.token import TokenData
# Settings
from app.core.settings import settings
# Config
from app.core.config import configuration
# Security
import fastapi.security as security
# JWT
from jose import JWTError, jwt
# Services
from app.services.auth import auth_service
# Routes
from app.api.routes.example import router as router_example
# DB
from app.db.db import db
