#!/usr/bin/env python3
'''
Copyright (C) 2024, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'ArvanCloud (ArvanCloud)'


def is_waf(self):
    if self.matchHeader(('Server', 'ArvanCloud')):
        return True

    return False