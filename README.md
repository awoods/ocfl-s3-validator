# python-package-template

A python packaging template to create new python packages

# Packaging

Read the instructions in the [LTS python package template](https://github.com/harvard-lts/python-package-template) for more information on how to build and publish python packages.

**Keep the link to the Packaging instructions above and replace everything below with specific app details**

# Quick start

A quick set of commands to run after initial setup is complete.

```
uv venv --python 3.12.0
source .venv/bin/activate
set -a && source .env && set +a
uv build
uv publish
```

# Installation

## Install uv package manager

https://docs.astral.sh/uv/

https://docs.astral.sh/uv/reference/settings/#publish-url

```
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### Install python

Install a specific python version on your local machine, if not installed already. Optionally, the `uv` package allows for installing multiple python versions.

```
uv python install 3.11 3.12
```

To view python installations run uv list.

```
uv python list
```

### Virtual environment

Create a new virtual environment with a specific python version.

```
uv venv --python 3.12.0
```

Activate the virtual environment

```
source .venv/bin/activate
```

### Add dependencies

Run the `uv add` command to add dependencies to the project.

This example adds [the `ruff` package which is an extremely fast python linter](https://docs.astral.sh/ruff/).

```
uv add ruff
```

Run the ruff check command

```
uv run ruff check
```

Read more about [managing dependencies in the documentation](https://docs.astral.sh/uv/guides/projects/#managing-dependencies).

### Test modules locally

Activate a virtual environment using the instructions above.

Navigate to the src directory and run a python interpreter.

```
cd src
python
```

Import the hello_world module from the python_package_template.

```
from python_package_template.hello_world import hello_world
```

Call hello_world()

```
hello_world()
```

Example output

```
src % python
Python 3.9.6 (default, Feb  3 2024, 15:58:27)
[Clang 15.0.0 (clang-1500.3.9.4)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> from python_package_template.hello_world import hello_world
>>> hello_world()
Hello from python-package-template!
```

### Project structure

Read more about the [project structure in the documentation](https://docs.astral.sh/uv/guides/projects/#project-structure).

## Packaging

### Build system

This project is already configured to use the default build system `hatchling` in the `[build-system]` section of the `pyproject.toml` file.

Read more about [build systems in the documentation](https://docs.astral.sh/uv/concepts/projects/config/#build-systems).

### Build project

Run uv build to build the project distribution files.

```
uv build
```

Read more about the [build command in the documentation](https://docs.astral.sh/uv/guides/publish/#building-your-package).

### Generate a token

Login to artifactory and click on the "Set me up" menu item on the top right

Select the lts-python repository

Generate a token

### Set environment variables and Artifactory authentication

Update the .env file

Set the username to your Artifactory username and set the password to the token value generated in JFrog Artifactory.

```
UV_PUBLISH_USERNAME={artifactory username}
UV_PUBLISH_PASSWORD={token generated in JFrog Artifactory}
```

Next, update the `.netrc` file with the same credentials:

```
login {artifactory username}
password {token generated in JFrog Artifactory}
```

Source the .env file

```
set -a && source .env && set +a
```

Make sure there are no spaces in the .env file for the source command to work correctly

**Important: Run `env` to list all of the variables to sure the variables are being set correctly**

### Set publish url

The publish URL is set to the HUIT artifactory already.

https://docs.astral.sh/uv/reference/settings/#publish-url

**Important: Make sure to delete old builds from the `dist/` folder or the publish will not work**

Run the uv sync command to make sure the uv.lock file is updated with the latest changes.

```
uv sync
```

Run the uv publish command with the settings in `pyproject.toml`.

```
uv publish
```

Optionally, to publish to a different repository, run the uv publish command and provide the url to the publish index directly.

```
uv publish --publish-url=https://artifactory.huit.harvard.edu/artifactory/api/pypi/lts-python
```

Note: The first time the package is published and error message may appear that the check-url could not be queried because the package does not exist. If this is the case, comment out check-url, publish the package, and then add it back in for later use.

### Installation

Read the instructions in the [python-package-demo](https://github.com/harvard-lts/python-package-demo) repository to install the package in another project.

Set the installation environment variables when installing from JFrog Artifactory.

https://github.com/astral-sh/uv/issues/8518
