#!/usr/bin/env python
from django.core.management import execute_from_command_line
import os
import sys
import imp

if __name__ == "__main__":
    imp.find_module('settings')
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
    execute_from_command_line(sys.argv)
