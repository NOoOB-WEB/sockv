"""
This file give us operating system name and details.
As using socket is different on unix and windows First we need to know the os
to use the right part of the code
"""

#importing platform for getting operating system details
import platform

#this error raise when a os operation fails 
OS_EXCEPTION = "Couldn't get the platform OS!"

class OS_Error(Exception):
    pass
#OS class had name and version attributes which we can use them to determine the os
class OS:
    def __init__(self):
        pass

    def determine_os(self):
        try:
            name = platform.system()
            version = platform.version()
            os = [name,version]
            return os
        except Exception as error:
            raise OS_Error(OS_EXCEPTION)