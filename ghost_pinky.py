"""
    Ghost: Pinky

    This file defines the frames for Pinky

"""

from sensible_colours import *
"""
SenseHAT Colours

These colours provide reasonable colour variation to be visible when
displayed on the SenseHAT.

The values of Red, Green and Blue that provide good variations are:

    0, 48, 96, 144, 192, 240, 255

"""

pinky_frames = [
    [
        k, k, p, p, p, pd, k, k,
        k, p, p, p, p, p, pd, k,
        p, p, w, k, p, w, k, pd,
        p, p, w, w, p, w, w, pd,
        p, p, p, p, p, p, pd, pd,
        p, p, p, p, p, p, pd, pd,
        p, p, p, p, p, p, pd, pd,
        p, k, p, p, k, p, pd, pd
    ],
    [
        k, k, p, p, p, pd, k, k,
        k, p, p, p, p, p, pd, k,
        p, p, w, k, p, w, k, pd,
        p, p, w, w, p, w, w, pd,
        p, p, p, p, p, p, pd, pd,
        p, p, p, p, p, p, pd, pd,
        p, p, p, p, p, p, pd, pd,
        p, k, p, p, p, k, pd, pd
    ],
    [
        k, k, p, p, p, pd, k, k,
        k, p, p, p, p, p, pd, k,
        p, p, k, w, p, k, w, pd,
        p, p, w, w, p, w, w, pd,
        p, p, p, p, p, p, pd, pd,
        p, p, p, p, p, p, pd, pd,
        p, p, p, p, p, p, pd, pd,
        p, p, k, p, p, p, k, pd
    ],
    [
        k, k, p, p, p, pd, k, k,
        k, p, p, p, p, p, pd, k,
        p, p, k, w, p, k, w, pd,
        p, p, w, w, p, w, w, pd,
        p, p, p, p, p, p, pd, pd,
        p, p, p, p, p, p, pd, pd,
        p, p, p, p, p, p, pd, pd,
        p, p, k, p, p, k, pd, pd
    ],

]
