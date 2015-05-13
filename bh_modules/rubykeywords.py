"""
BracketHighlighter.

Copyright (c) 2013 - 2015 Isaac Muse <isaacmuse@gmail.com>
License: MIT
"""
import re


def post_match(view, name, style, first, second, center, bfr, threshold):
    """Strip whitespace from being targeted with highlight."""

    if first is not None:
        # Strip whitespace from the beginning of first bracket
        open_bracket = bfr[first.begin:first.end]
        if open_bracket != "do":
            m = re.match(r"(\s*\b)[\w\W]*", open_bracket)
            if m:
                first = first.move(first.begin + m.end(1), first.end)
    return first, second, style
