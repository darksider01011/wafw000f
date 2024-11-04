#!/usr/bin/env python3
'''
Copyright (C) 2024, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

from dataclasses import asdict, dataclass, fields
from random import randint

from wafw00f import __version__


@dataclass
class Color:
    """ANSI colors."""
    W: str = '\033[1;97m'
    Y: str = '\033[1;93m'
    G: str = '\033[1;92m'
    R: str = '\033[1;91m'
    B: str = '\033[1;94m'
    C: str = '\033[1;96m'
    E: str = '\033[0m'

    @classmethod
    def disable(cls):
        """Disables all colors."""
        cls.W = ''
        cls.Y = ''
        cls.G = ''
        cls.R = ''
        cls.B = ''
        cls.C = ''
        cls.E = ''

    @classmethod
    def unpack(cls):
        """Unpacks and returns the color values.
        Useful for brevity, e.g.:
        (W,Y,G,R,B,C,E) = Color.unpack()
        """
        return (cls.W,
                cls.Y,
                cls.G,
                cls.R,
                cls.B,
                cls.C,
                cls.E
                )




def randomArt():
    return None
