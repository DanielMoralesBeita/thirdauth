#!/usr/bin/env python
import os
import sys
#import debug_toolbar.models

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "thirdauth.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
