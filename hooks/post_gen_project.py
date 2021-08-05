import os

os.system("dotnet new nugetconfig")

print("""
You should run the following command:

dotnet nuget add source https://pkgs.dev.azure.com/{{cookiecutter.organization_name}}/{{cookiecutter.team_project_name}}/_packaging/{{cookiecutter.project_feed_name}}/nuget/v3/index.json --name WHATEVER_YOU_WANT --username YOUR_USER_NAME --password YOUR_PAT --configfile nuget.config
""")
