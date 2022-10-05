import os
import shutil


curdir = os.path.realpath(os.path.curdir)
if "{{cookiecutter.workflow}}" == "github":
    shutil.rmtree(os.path.join(curdir, ".github"))
else:
    os.remove(os.path.join(curdir, "azure-pipelines.yml"))
