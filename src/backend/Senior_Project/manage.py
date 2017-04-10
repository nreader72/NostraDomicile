#!/usr/bin python2.7
import os
import sys
#import django

if __name__ == "__main__":


    from django.core.management import execute_from_command_line
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "NostraDomicile.settings")
    execute_from_command_line(sys.argv)

