import sys


def is_empty(value):
    return not value.strip()


if is_empty("{{cookiecutter.package_name}}"):
    print("ERROR: package_name is not valid.")
    sys.exit(1)
if is_empty("{{cookiecutter.organization_name}}"):
    print("ERROR: organization_name is not valid.")
    sys.exit(1)
if is_empty("{{cookiecutter.feed_name}}"):
    print("ERROR: feed_name is not valid.")
    sys.exit(1)
if is_empty("{{cookiecutter.workflow}}"):
    print("ERROR: workflow is not valid.")
    sys.exit(1)
