Logger Class

A simple Logger class in Python to manage and filter log messages based on their timestamps.


Description

This Logger class is designed to track messages and decide whether a message should be printed based on a specified timestamp. Each message is allowed to be printed once every 10 seconds. The class also includes methods to clear the log and to check the current size of the logger.


Installation

To use this Logger class, simply copy the logger.py file into your project directory and import it.



Usage

Creating an instance of Logger:

logger = Logger()

Checking if a message should be printed:

timestamp = 1
message = "foo"
should_print = logger.shouldPrintMessage(timestamp, message)
print(should_print)

Cleaning the logger based on the timestamp:

timestamp = 12
is_cleaned = logger.clean(timestamp)
print(is_cleaned)

Getting the current size of the logger:

size = logger.loggerSize()
print(size) 


Example

Here's a complete example demonstrating how to use the Logger class:

class Logger():

    def __init__(self):
        self.messages = dict()
        self.timestamp = 0

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.messages or self.messages[message] <= timestamp:
            self.timestamp = timestamp
            self.messages[message] = timestamp + 10
            return True[Uploading logger.py…]()class Logger():
    def __init__(self):
        self.messages = dict()
        self.timestamp = 0

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.messages or self.messages[message] <= timestamp:
            self.timestamp = timestamp
            self.messages[message] = timestamp + 10
            return True
        else:
            return False

    def clean(self, timestamp: int) -> bool:
        if self.timestamp < timestamp:
            self.messages.clear()
            self.timestamp = 0
            return True
        else:
            return False

    def loggerSize(self) -> int:
        return len(self.messages)

logger = Logger()

print(logger.shouldPrintMessage(1, "foo"))  # True
print(logger.shouldPrintMessage(2, "bar"))  # True
print(logger.shouldPrintMessage(3, "foo"))  # False
print(logger.shouldPrintMessage(8, "bar"))  # False
print(logger.shouldPrintMessage(10, "foo")) # False
print(logger.shouldPrintMessage(11, "foo")) # True

print(logger.loggerSize())  # 2
print(logger.clean(11))     # False
print(logger.clean(12))     # True
