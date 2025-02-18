# Copyright (c) 2022-2024, NVIDIA CORPORATION. All rights reserved.

.PHONY: clean test coverage build install lint docs help

.DEFAULT_GOAL := help

define BROWSER_PYSCRIPT
import os, webbrowser, sys

from urllib.request import pathname2url

webbrowser.open("file://" + pathname2url(os.path.abspath(sys.argv[1])))
endef
export BROWSER_PYSCRIPT

define PRINT_HELP_PYSCRIPT
import re, sys

for line in sys.stdin:
	match = re.match(r'^([a-zA-Z_-]+):.*?## (.*)$$', line)
	if match:
		target, help = match.groups()
		print("%-20s %s" % (target, help))
endef
export PRINT_HELP_PYSCRIPT

BROWSER := python -c "$$BROWSER_PYSCRIPT"

help:
	@python -c "$$PRINT_HELP_PYSCRIPT" < $(MAKEFILE_LIST)

# ============================================================================ #
# CLEAN COMMANDS
# ============================================================================ #

clean: clean-build clean-pyc ## remove all build, test, coverage and Python artifacts

clean-build: ## remove build artifacts
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -f {} +

clean-pyc: ## remove Python file artifacts
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

# ============================================================================ #
# BUILD COMMANDS
# ============================================================================ #

build: clean ## builds source and wheel package
	python3 -m build --verbose --wheel
	ls -l dist

build-no-isolation: clean ## builds source and wheel package
	python3 -m build --verbose --no-isolation --wheel
	ls -l dist

build-sdist: clean ## builds source and wheel package
	python3 -m build --verbose --no-isolation --sdist
	ls -l dist

# ============================================================================ #
# INSTALL COMMANDS
# ============================================================================ #

install: clean ## install the package to the active Python's site-packages
	pip install -e .