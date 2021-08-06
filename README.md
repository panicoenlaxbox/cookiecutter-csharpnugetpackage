# Introduction

A [cookiecutter](https://github.com/cookiecutter/cookiecutter) template for a NuGet package published in Azure DevOps.

[Related post](https://www.panicoenlaxbox.com/post/nuget-package-azure-devops/)

# Usage

```bash
pip install cookiecutter
cookiecutter https://github.com/panicoenlaxbox/cookiecutter-csharpnugetpackage
```

## Parameters

| Parameter | Description |
| -------------- | ------------------------------------------------------------ |
| `package_name` | Package name |
| `organization_name` | Azure DevOps organization name |
| `team_project_name` | Azure DevOps team project name |
| `project_feed_name` | Azure DevOps project feed name |

## nuget.config

`nuget.config` file is just the output of `dotnet new nugetconfig`, so we must add a valid source in order to publish our package.

For this purpose, we can use `dotnet nuget add source` like so:

```bash
dotnet nuget add source https://pkgs.dev.azure.com/YOUR_ORGANIZATION/YOUR_TEAM_PROJECT/_packaging/YOUR_PROJECT_FEED/nuget/v3/index.json --name WHATEVER_YOU_WANT --username YOUR_USER_NAME --password YOUR_PAT --configfile nuget.config
```

> PAT is a Personal access token.

At this moment, you will have your source saved in the `nuget.config` file in the project's root folder.

`nuget.config` file is excluded in the git repository.

```bash
# Nuget personal access tokens and Credentials
nuget.config
```

If you don't want to use this `nuget.config` file, you can remove it and use any other `nuget.config` in the hierarchy, more info at https://docs.microsoft.com/en-us/nuget/consume-packages/configuring-nuget-behavior#config-file-locations-and-uses

## Testing

```bash
dotnet test /p:CollectCoverage=true /p:CoverletOutputFormat=cobertura /p:CoverletOutput=..\TestResults\Coverage\
```

Previous command will generate 'coverage.cobertura.xml' file in the specified folder.

Now, we can run the following command to generate a HTML file with our testing coverage.

```bash
dotnet reportgenerator -reports:tests\TestResults\Coverage\**\*.cobertura.xml -targetdir:tests\TestResults\reportgenerator -reporttypes:HtmlInline_AzurePipelines
```

`TestResults` folder is excluded also in the git repository.

```bash
# MSTest test Results
[Tt]est[Rr]esult*/
```

## Azure DevOps

You must create, in addition to the team project, a project feed and an environment with manual approval.

With everything ready, you can now create the pipeline using the `azure-pipelines.yml` file, where you will have to select the id of the just created feed and write the right environment name.

The pipeline needs the following variables ir order to run successfully:

| Name                 | Value                                                        |
| -------------------- | ------------------------------------------------------------ |
| `Major`              | 0                                                            |
| `Minor`              | 0                                                            |
| `PackageVersionType` |                                                              |
| `Patch`              | `$[counter(format('{0}.{1}', variables['Major'], variables['Minor']), 0)]` |
| `PackageVersion`     | `$(Major).$(Minor).$(Patch)$(PackageVersionType)`            |

> The idea comes from https://www.koskila.net/fun-with-azure-devops-nuget-package-versioning/

`PackageVersionType` should be empty or something like -value (hyphen included), more info at https://docs.microsoft.com/en-us/nuget/create-packages/prerelease-packages. Currently, if you don't supply any value and the triggered branch is not `main`, the variable will be set to `-alpha`.

You should allow to modify in each pipeline execution (*Let users override this value when running this pipeline*), the values of `Major`, `Minor` and `PackageVersionType` variables to control SEMVER package version manually when required.

## Visual Studio

From a client application, you can debug your package in Visual Studio enabling Source Link support. More info at https://lurumad.github.io/using-source-link-in-net-projects-and-how-to-configure-visual-studio-to-use-it

The following configuration has to be done in Visual Studio.

- Enable Just My Code (disabled)
- Enable Source Link support (enabled)

To support source link, you can see that we had to add the following to the `.csproj` file.

```xml
<PropertyGroup>
    <DebugType>embedded</DebugType>
    <DebugSymbols>true</DebugSymbols>
    <PublishRepositoryUrl>true</PublishRepositoryUrl>
    <ContinuousIntegrationBuild Condition="'$(TF_BUILD)' == 'true'">True</ContinuousIntegrationBuild>
    <Deterministic>true</Deterministic>
    <EmbedUntrackedSources>true</EmbedUntrackedSources>
    <Version>1.0.0</Version>
</PropertyGroup>
```

You should see something similar to this in your package, once published.

![](docs/images/Package.png)
