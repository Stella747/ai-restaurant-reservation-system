"""Initialize AWS session and DynamoDB table (run before starting the API)."""

import os

import boto3
from dotenv import load_dotenv

import src.database.setup_database as setup_database

load_dotenv()

setup_database.setup_restaurant_reservation_table()

region = os.getenv("AWS_REGION", "us-east-1")
boto3.setup_default_session(region_name=region)