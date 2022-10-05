import os
import shutil


curdir = os.path.realpath(os.path.curdir)
if "{{cookiecutter.workflow}}" == "github":
    os.remove(os.path.join(curdir, "azure-pipelines.yml"))
else:
    shutil.rmtree(os.path.join(curdir, ".github"))
