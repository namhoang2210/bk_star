import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

_env = os.environ.get

POSTGRES_DB = _env("POSTGRES_DB")
POSTGRES_HOST = _env("POSTGRES_HOST")
POSTGRES_USER = _env("POSTGRES_USER")
POSTGRES_PASSWORD = _env("POSTGRES_PASSWORD")
POSTGRES_PORT = _env("POSTGRES_PORT")

APP_ENV = _env("APP_ENV")
WEB_URL = _env("WEB_URL")
# API_INVOICE_URL = _env("API_INVOICE_URL")
PROJECT_NAME = _env("PROJECT_NAME")
LANGUAGE = _env("LANGUAGE")

# AWS_COGNITO_ACCESS_KEY = _env("AWS_COGNITO_ACCESS_KEY")
# AWS_COGNITO_SECRET_KEY = _env("AWS_COGNITO_SECRET_KEY")
# AWS_COGNITO_REGION = _env("AWS_COGNITO_REGION")
# AWS_COGNITO_USERPOOL_ID = _env("AWS_COGNITO_USERPOOL_ID")
# AWS_COGNITO_USER_GROUP = _env("AWS_COGNITO_USER_GROUP")
# AWS_COGNITO_S2S_CLIENT_KEY = _env("AWS_COGNITO_S2S_CLIENT_KEY")
# AUTH_CACHE_TTL = _env("AUTH_CACHE_TTL")
#
# REDIS_DB = _env("REDIS_DB")
# REDIS_HOST = _env("REDIS_HOST")
# REDIS_PORT = _env("REDIS_PORT")
#
# TOKEN_GENERATION_KEY = _env("TOKEN_GENERATION_KEY")
#
# AWS_ACCESS_KEY = _env("FILES_SERVICE_AWS_ACCESS_KEY")
# AWS_SECRET_KEY = _env("FILES_SERVICE_AWS_SECRET_ACCESS_KEY")
# S3_BUCKET_NAME = _env("S3_BUCKET_NAME")
# S3_REGION = _env("S3_REGION")
#
# AWS_SNS_SECRET_KEY = _env("AWS_SNS_SECRET_KEY")
# AWS_SNS_ACCESS_KEY = _env("AWS_SNS_ACCESS_KEY")
# SNS_REGION = _env("SNS_REGION")
# TOPIC_OOPS = _env("TOPIC_OOPS")
#
# THUMBNAIL_SERVICE_AWS_ACCESS_KEY = _env("THUMBNAIL_SERVICE_AWS_ACCESS_KEY")
# THUMBNAIL_SERVICE_AWS_SECRET_KEY = _env("THUMBNAIL_SERVICE_AWS_SECRET_KEY")
# THUMBNAIL_SERVICE_S3_BUCKET_NAME = _env("THUMBNAIL_SERVICE_S3_BUCKET_NAME")
# THUMBNAIL_SERVICE_S3_REGION = _env("THUMBNAIL_SERVICE_S3_REGION")
# THUMBNAIL_SERVICE_CLOUDFRONT_DOMAIN = _env(
#     "THUMBNAIL_SERVICE_CLOUDFRONT_DOMAIN"
# )
# URL_GET_TOKEN = _env("URL_GET_TOKEN")
# CLIENT_SECRET = _env("CLIENT_SECRET")
# CLIENT_KEY = _env("CLIENT_KEY")
# URL_INVOICE_SERVICE = _env("URL_INVOICE_SERVICE")
