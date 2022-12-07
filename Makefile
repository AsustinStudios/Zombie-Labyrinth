SHELL := /bin/bash

current_dir = $(shell pwd)
PYTHON = /usr/bin/env PYTHONPATH=. $(shell pwd)/.virtualenv/bin/python

DEFAULT: tasks

clean: nuke-pyc

developer-setup:
	virtualenv --python=/usr/bin/python3 .virtualenv
	source .virtualenv/bin/activate
	.virtualenv/bin/pip install -r requirements.txt -r requirements-dev.txt
	.virtualenv/bin/pip install -e .

make pip-compile: pip-compile-app pip-compile-dev
	git diff --color=always --exit-code requirements.txt requirements-dev.txt

pip-compile-app: __pip-compile-app
	git diff --color=always --exit-code requirements.txt

__pip-compile-app:
	@.virtualenv/bin/pip-compile --verbose --allow-unsafe --no-emit-trusted-host --upgrade --output-file requirements.txt requirements.in

pip-compile-dev: __pip-compile-app
	git diff --color=always --exit-code requirements-dev.txt

__pip-compile-dev:
	@.virtualenv/bin/pip-compile --verbose --allow-unsafe --no-emit-trusted-host --upgrade --output-file requirements-dev.txt requirements-dev.in

nuke-pyc:
	@find src -name '*.pyc' -exec unlink '{}' \;

tasks:
	@echo 'clean                                    Delete temp files'
	@echo 'developer-setup                          Setup virtualenv and install dependencies'
	@echo 'pip-compile                              Update versions of python dependencies in requirements.txt'
