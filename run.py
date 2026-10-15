#!/usr/bin/env python
import os
import sys

def main():
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    if len(sys.argv) <= 1:
        args = [sys.argv[0], "runserver", "127.0.0.1:8000"]
    else:
        args = sys.argv
    execute_from_command_line(args)

if __name__ == "__main__":
    main()
