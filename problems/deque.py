from collections import deque

"""
>>> queue = TicketQueue()
>>> queue.add_person("Jack")
Jack has been added to the queue

>>> queue = TicketQueue()
>>> queue.add_person("Jack")
Jack has been added to the queue
>>> queue.service_person()
Jack has been serviced

>>> queue = TicketQueue()
>>> queue.add_person("Jack")
Jack has been added to the queue
>>> queue.bypass_queue("Jill")
Jill has bypassed the queue
"""

class TicketQueue(object):
    def __init__(self):
        self.deque = deque()

    def add_person(self, name):
        pass

    def service_person(self):
        pass

    def bypass_queue(self, name):
        pass
