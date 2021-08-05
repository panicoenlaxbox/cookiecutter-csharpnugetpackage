import sys


if not '{{cookiecutter.package_name}}'.strip():
    print('ERROR: package_name is not valid.')
    sys.exit(1)
