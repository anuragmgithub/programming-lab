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

