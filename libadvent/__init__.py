"""Helper library for Advent of Code"""
from os import environ, getenv

import requests
from dotenv import load_dotenv

load_dotenv(verbose=True)
AOC_SESSION = getenv("AOC_SESSION")
if not AOC_SESSION:
    raise RuntimeError("AOC_SESSION environment variable is not set")

session = requests.Session()
session.cookies.set("session", AOC_SESSION)
