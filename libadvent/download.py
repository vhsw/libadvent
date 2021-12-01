#!/usr/bin/env python3
"""Download input data and create answer template"""

import argparse
import importlib
import re
from datetime import datetime
from os import makedirs

from bs4 import BeautifulSoup

from . import session, templates


def download(date: datetime):
    directory = create_dir(date)
    task = download_task(date)
    title = get_title(task)
    module = sanitize(title)
    input_path = f"{directory}/input.txt"
    with open(f"{directory}/{module}.py", "w", encoding="utf-8") as fp:
        fp.write(
            importlib.resources.read_text(templates, "solution.py").format(
                day=date.day, input_path=input_path, title=title
            )
        )
    with open(f"{directory}/{module}_test.py", "w", encoding="utf-8") as fp:
        fp.write(
            importlib.resources.read_text(templates, "test.py").format(
                day=date.day, module=module
            )
        )
    with open(input_path, "w", encoding="utf-8") as fp:
        fp.write(download_input(date))


def create_dir(date: datetime) -> str:
    directory = f"{date.year}/Day {date.day:02d}"
    makedirs(directory)
    return directory


def download_task(date: datetime) -> str:
    url = f"https://adventofcode.com/{date.year}/day/{date.day}"
    response = session.get(url)
    response.raise_for_status()
    return response.text


def download_input(date: datetime) -> str:
    url = f"https://adventofcode.com/{date.year}/day/{date.day}/input"
    response = session.get(url)
    response.raise_for_status()
    return response.text


def get_title(task: str) -> str:
    soup = BeautifulSoup(task, "lxml")
    header = soup.select_one("body > main > article > h2").get_text()
    if match := re.match(r"--- Day \d+: (.+) ---", header):
        return match.group(1)
    raise ValueError(f"{header=} is not valid")


def sanitize(title: str) -> str:
    return re.sub(r"\W+", "_", title).lower().strip("_")


def cli():
    """Console handler"""
    parser = argparse.ArgumentParser(description="Download task from Advent of Code")
    parser.add_argument(
        "date",
        type=lambda v: datetime.strptime(v, "%Y-%m-%d"),
        default=datetime.now(),
        nargs="?",
        help="date in format YYYY-mm-dd",
    )
    args = parser.parse_args()
    download(args.date)


if __name__ == "__main__":
    cli()
