"""Easter Eggs extractor"""
import argparse
from datetime import datetime

from bs4 import BeautifulSoup

from libadvent import session


def main():
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
    _download(args.date)


def _download(date: datetime):
    url = f"https://adventofcode.com/{date.year}/day/{date.day}"
    req = session.get(url)
    soup = BeautifulSoup(req.text, "lxml")
    for p_tag in soup.select("p"):
        for span in p_tag.select("span"):
            if text := span.get("title"):
                span.replace_with(f"{span.get_text()} (egg: {text})")
                print(p_tag.get_text())
