"""Conservative X weighted length for short Japanese posts and ASCII URLs.

NFC and single-weight ranges follow twitter-text v3. Emoji sequences may be
overcounted; never treat this helper as an exact emoji/URL parser.
Reference: https://docs.x.com/fundamentals/counting-characters
"""

import re
import unicodedata

URL = re.compile(r"https?://[A-Za-z0-9:/?#\[\]@!$&'()*+,;=._~%+-]+")
SINGLE = ((0, 4351), (8192, 8205), (8208, 8223), (8242, 8247))


def weighted_length(text: str) -> int:
    text = unicodedata.normalize("NFC", text)
    # Count URLs as 23 single-weight placeholders; Unicode text is never swallowed.
    text = URL.sub("x" * 23, text)
    return sum(1 if any(lo <= ord(c) <= hi for lo, hi in SINGLE) else 2 for c in text)
