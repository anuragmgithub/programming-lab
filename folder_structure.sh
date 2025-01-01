#!/bin/bash

# Define project name
PROJECT_NAME="file-manager-cli"

# Create the main project directory
mkdir $PROJECT_NAME

# Create the package directory
mkdir $PROJECT_NAME/file_manager_cli

# Create package files
touch $PROJECT_NAME/file_manager_cli/__init__.py
touch $PROJECT_NAME/file_manager_cli/cli.py
touch $PROJECT_NAME/file_manager_cli/file_operations.py
touch $PROJECT_NAME/file_manager_cli/utils.py

# Create the test directory
mkdir $PROJECT_NAME/tests
touch $PROJECT_NAME/tests/__init__.py
touch $PROJECT_NAME/tests/test_file_operations.py

# Create setup files
touch $PROJECT_NAME/setup.py
touch $PROJECT_NAME/MANIFEST.in
touch $PROJECT_NAME/requirements.txt
touch $PROJECT_NAME/README.md
touch $PROJECT_NAME/.gitignore

# Inform the user that the setup is complete
echo "Project structure for $PROJECT_NAME has been created."
