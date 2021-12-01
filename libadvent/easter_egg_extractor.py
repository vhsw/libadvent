#!/usr/bin/env python3
"""Easter Eggs extractor"""
import argparse
from datetime import datetime

from bs4 import BeautifulSoup

from . import session


def download(date: datetime):
    url = f"https://adventofcode.com/{date.year}/day/{date.day}"
    req = session.get(url)
    soup = BeautifulSoup(req.text, "lxml")
    for p in soup.select("p"):
        for span in p.select("span"):
            text = span.get("title")
            if text:
                span.replace_with(f"{span.get_text()} (egg: {text})")
                print(p.get_text())


def cli():
    """Console handler"""
    parser = argparse.ArgumentParser(
        description="Download Easter Eggs from Advent of Code"
    )
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
