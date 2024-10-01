# # -*- coding: utf-8 -*-

# """ pySim: various utilities
# """

# import json
# import abc
import string

# from io import BytesIO
from typing import Optional, List, Dict, Any, Tuple


# # just to differentiate strings of hex nibbles from everything else
Hexstr = str


def h2b(s: Hexstr) -> bytearray:
    """convert from a string of hex nibbles to a sequence of bytes"""
    return bytearray.fromhex(s)


def b2h(b: bytearray) -> Hexstr:
    """convert from a sequence of bytes to a string of hex nibbles"""
    return "".join(["%02x" % (x) for x in b])


def h2i(s: Hexstr) -> List[int]:
    """convert from a string of hex nibbles to a list of integers"""
    return [(int(x, 16) << 4) + int(y, 16) for x, y in zip(s[0::2], s[1::2])]


def i2h(s: List[int]) -> Hexstr:
    """convert from a list of integers to a string of hex nibbles"""
    return "".join(["%02x" % (x) for x in s])


def h2s(s: Hexstr) -> str:
    """convert from a string of hex nibbles to an ASCII string"""
    return "".join(
        [
            chr((int(x, 16) << 4) + int(y, 16))
            for x, y in zip(s[0::2], s[1::2])
            if int(x + y, 16) != 0xFF
        ]
    )


def s2h(s: str) -> Hexstr:
    """convert from an ASCII string to a string of hex nibbles"""
    b = bytearray()
    b.extend(map(ord, s))
    return b2h(b)


def i2s(s: List[int]) -> str:
    """convert from a list of integers to an ASCII string"""
    return "".join([chr(x) for x in s])


def swap_nibbles(s: Hexstr) -> Hexstr:
    """swap the nibbles in a hex string"""
    return "".join([x + y for x, y in zip(s[1::2], s[0::2])])


def rpad(s: str, l: int, c="f") -> str:
    """pad string on the right side.
    Args:
            s : string to pad
            l : total length to pad to
            c : padding character
    Returns:
            String 's' padded with as many 'c' as needed to reach total length of 'l'
    """
    return s + c * (l - len(s))


def str_sanitize(s: str) -> str:
    """replace all non printable chars, line breaks and whitespaces, with ' ', make sure that
    there are no whitespaces at the end and at the beginning of the string.

    Args:
            s : string to sanitize
    Returns:
            filtered result of string 's'
    """

    chars_to_keep = string.digits + string.ascii_letters + string.punctuation
    res = "".join([c if c in chars_to_keep else " " for c in s])
    return res.strip()


def sw_match(sw: str, pattern: str) -> bool:
    """Match given SW against given pattern."""
    # Create a masked version of the returned status word
    sw_lower = sw.lower()
    sw_masked = ""
    for i in range(0, 4):
        if pattern[i] == "?":
            sw_masked = sw_masked + "?"
        elif pattern[i] == "x":
            sw_masked = sw_masked + "x"
        else:
            sw_masked = sw_masked + sw_lower[i]
    # Compare the masked version against the pattern
    return sw_masked == pattern
