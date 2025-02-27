# Copyright 2015-2021 the openage authors. See copying.md for legal info.

"""
Various OS utilities
"""

import re
from sys import platform

from .math import INF


def free_memory():
    """
    Returns the amount of free bytes of memory.
    On failure, returns +inf.

    >>> free_memory() > 0
    True
    """
    memory = INF

    if platform.startswith('linux'):
        pattern = re.compile('^MemAvailable: +([0-9]+) kB\n$')
        with open('/proc/meminfo', encoding='utf8') as meminfo:
            for line in meminfo:
                match = pattern.match(line)
                if match:
                    memory = 1024 * int(match.group(1))
                    break
    elif platform == "darwin":
        # TODO
        pass
    elif platform == "win32":
        # TODO
        pass

    return memory
