"""Update stats section in README.md"""
import re

from bs4 import BeautifulSoup

from libadvent import session


def main():
    """Fetch star counters and update README"""
    url = "https://adventofcode.com/events"
    req = session.get(url)
    soup = BeautifulSoup(req.text, "lxml")
    stats = soup.select('body > main > article > div[class="eventlist-event"]')
    text = "## Statistics\n\n"
    total = 0
    for element in stats:
        line = element.get_text()
        year, stars = re.match(r"\[(\d{4})\] +(\d+)?", line).groups()
        if not stars:
            stars = 0
        stars = int(stars)
        total += stars
        badge = ":star2:" if stars == 50 else ":star:"
        text += f"- {year}: {stars:02d} {badge}\n"
    text += f"\nTotal stars: {total} :star:\n"
    with open("README.md", encoding="utf-8") as fp:
        data = fp.read()
        head, _ = data.rsplit("## Statistics", 1)
    with open("README.md", "w", encoding="utf-8") as fp:
        fp.write(head + text)
