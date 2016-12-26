#!/usr/bin/env python

class Frame(object):
    def __init__(self, frame, timestamp, ideal_fps, real_fps, xres, yres):
        self.frame = frame
        self.timestamp = timestamp
        self.ideal_fps = ideal_fps
        self.real_fps = real_fps
        self.xres = xres
        self.yres = yres

