SHELL := /bin/bash

current_dir = $(shell pwd)
PYTHON = /usr/bin/env PYTHONPATH=. $(shell pwd)/.virtualenv/bin/python

DEFAULT: tasks

# Developer Setup ##############################################################

clean: nuke-pyc
	@rm -r zombie_labyrinth.egg-info

developer-setup:
	virtualenv --python=/usr/bin/python3 .virtualenv
	source .virtualenv/bin/activate
	.virtualenv/bin/pip install -r requirements.txt -r requirements-dev.txt
	.virtualenv/bin/pip install -e .

pip-compile: __pip-compile-app __pip-compile-dev
	git diff --color=always --exit-code requirements.txt requirements-dev.txt

pip-compile-app: __pip-compile-app
	git diff --color=always --exit-code requirements.txt

__pip-compile-app:
	@.virtualenv/bin/pip-compile --verbose --allow-unsafe --no-emit-trusted-host --upgrade --output-file requirements.txt requirements.in

pip-compile-dev: __pip-compile-dev
	git diff --color=always --exit-code requirements-dev.txt

__pip-compile-dev:
	@.virtualenv/bin/pip-compile --verbose --allow-unsafe --no-emit-trusted-host --upgrade --output-file requirements-dev.txt requirements-dev.in

nuke-pyc:
	@find zombie_labyrinth -name '*.pyc' -exec unlink '{}' \;

pip-sync:
	@.virtualenv/bin/pip-sync requirements.txt requirements-dev.txt
	@.virtualenv/bin/pip install -e . --use-pep517


# Code checks ##################################################################

check-code: check-pep8 check-mypy

check-pep8:
	@.virtualenv/bin/ruff check .

check-mypy:
	@.virtualenv/bin/mypy -p zombie_labyrinth

# Tests ########################################################################

run-tests: check-code
	@.virtualenv/bin/pytest -p no:cacheprovider --durations=20 --cov --cov-report=term zombie_labyrinth/tests


tasks:
	@echo 'clean                                    Delete temp files'
	@echo 'developer-setup                          Setup virtualenv and install dependencies'
	@echo 'pip-compile                              Update versions of python dependencies in requirements.txt'
