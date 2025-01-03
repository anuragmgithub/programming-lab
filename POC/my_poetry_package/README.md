# My Poetry Package

This repository demonstrates how to create and build a Python package using **Poetry**. It covers the installation process, package setup, dependencies, and building the package.

## Table of Contents

- [Poetry Installation](#poetry-installation)
- [Setting Up the Project](#setting-up-the-project)
- [Project Structure](#project-structure)
- [Building the Package](#building-the-package)
- [Publishing the Package](#publishing-the-package)

## Poetry Installation

Poetry is a modern tool for Python dependency management and packaging. To install Poetry, follow these steps:

1. Open your terminal.
2. Run the following command to install Poetry:

    ```bash
    curl -sSL https://install.python-poetry.org | python3 -
    ```

3. After installation, verify Poetry was installed successfully:

    ```bash
    poetry --version
    ```

## Setting Up the Project

### 1. **Create a New Directory for the Package**

```bash
mkdir my_poetry_package
cd my_poetry_package
```
##  Initialize the Package with Poetry  

poetry init --no-interaction

### Install Dependencies  
poetry add requests  

### Building the Package  
poetry build  

### Installing the Package Locally  
poetry install

## setup.py vs poetry:  
Dependency Management  
Setuptools:  
Relies on requirements.txt or manual dependency management.  
Does not inherently support locking dependencies, making dependency resolution less robust.  
Poetry:  
Provides integrated dependency management and resolution.  
Uses poetry.lock to lock exact dependency versions, ensuring reproducible builds.  
Building the Package:  
Setuptools:  
Run the following to build the package:
```
python setup.py sdist bdist_wheel
```  
The distribution files are generated in the dist/ directory.
Poetry:  
Run the following to build the package:  
```
poetry build
```
This also generates distribution files in the dist/ directory.

Publishing:  
Publishing to PyPI often requires tools like twine:  
```
twine upload dist/*
```  

Poetry:  
Built-in support for publishing:  
```
poetry publish --build
```  

Virtual Environment Management:  
Setuptools:  
Does not include built-in support for managing virtual environments.  
rely on external tools like virtualenv or venv.  

Poetry:
Automatically creates and manages a virtual environment for your project:  
```
poetry install  
poetry shell  
```

## Dependency Management in Setuptools vs Poetry:  
Defining Dependencies:  

With setuptools, dependencies are typically defined in the install_requires parameter of setup.py.  
Alternatively, a requirements.txt file is used to list dependencies separately.  
```
from setuptools import setup

setup(
    name="mypackage",
    version="0.1.0",
    description="A simple Python package",
    install_requires=[
        "requests>=2.0",  # Minimum version of requests is 2.0
        "numpy",          # Latest version of numpy
    ],
)
```

Example requirements.txt:   
```
requests>=2.0
numpy
pandas>=1.1,<2.0  # Specific version range
```

Installing Dependencies:  
If install_requires is used, dependencies are installed when the package itself is installed:  
pip install .  

If requirements.txt is used:  
pip install -r requirements.txt

Dependency Locking:  

Setuptools does not natively support dependency locking (ensuring that specific versions of dependencies are used across environments).
To achieve reproducible builds, you need tools like pip freeze to create a requirements.txt with specific versions:  
```
pip freeze > requirements.txt
````

Poetry Dependency Management:  
With Poetry, dependencies are declared in pyproject.toml under [tool.poetry.dependencies].  
```
[tool.poetry]
name = "mypackage"
version = "0.1.0"
description = "A simple Python package"

[tool.poetry.dependencies]
python = "^3.8"
requests = "^2.0"  # Automatically resolves the latest compatible version
numpy = "*"        # Any version
pandas = ">=1.1,<2.0"
```  
Installing Dependencies:  
```
poetry install  
```
Dependency Locking:  
Poetry automatically generates a poetry.lock file during dependency resolution.
This file locks all dependency versions (including sub-dependencies) to ensure reproducibility.  
```
[[package]]
name = "requests"
version = "2.25.1"
description = "Python HTTP library"
category = "main"
optional = false
python-versions = ">=3.6"

[[package]]
name = "numpy"
version = "1.20.3"
description = "Array processing for numbers"
category = "main"
optional = false
python-versions = ">=3.6"
```
Reproducible Builds:  
To replicate an environment exactly:  
poetry install  

Poetry reads the poetry.lock file and installs the exact versions listed, ensuring the same behavior across systems.

pip freeze:  
1. pip freeze scans the site-packages directory of the current Python environment to identify all installed packages.  
2. It outputs a list of package names and their specific versions in a format that pip install can understand.

Reproducible Environments:  
Save the output of pip freeze to a requirements.txt file to recreate the same environment later:  
```
pip freeze > requirements.txt
```

Install these exact versions in another environment:  
```
pip install -r requirements.txt  
```












