#!/usr/bin/env python

import time


class Profiler(object):
    def __init__(self, profiler_name=""):
        self.name = profiler_name
        self.clear()

    def register(self, name):
        now = time.clock()
        if name not in self.event_names:
            self.event_names[name] = len(self.events)
            if self.last_event is not None:
                self.events.append([name, now - self.last_event])
            else:
                self.events.append([name, 0])
        else:
            self.events[self.event_names[name]][1] += now - \
                self.last_event
        self.last_event = now

    def clear(self):
        self.events = []
        self.event_names = {}
        self.last_event = None

    def profile(self):
        if len(self.events) > 0:
            total_time = 0
            for i in range(0, len(self.events)):
                total_time += self.events[i][1]
            profile_str = "Profiling {}".format(self.name)
            profile_str += "\n\tTotal: {}".format(total_time)

            for i in range(0, len(self.events)):
                profile_str += ("\n\t" +
                                self.events[i][0] + " " +
                                str(self.events[i][1]) + " " +
                                "{0:.2f}".format(
                                    self.events[i][1] / total_time * 100) +
                                "%")
            return profile_str
        else:
            return ("Nothing to profile!")
