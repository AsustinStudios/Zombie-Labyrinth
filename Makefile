SHELL := /bin/bash

current_dir = $(shell pwd)
PYTHON = /usr/bin/env PYTHONPATH=. $(shell pwd)/.virtualenv/bin/python

DEFAULT: tasks

clean: nuke-pyc
	@rm -r zombie_labyrinth.egg-info

developer-setup:
	virtualenv --python=/usr/bin/python3 .virtualenv
	source .virtualenv/bin/activate
	.virtualenv/bin/pip install -r requirements.txt -r requirements-dev.txt
	.virtualenv/bin/pip install -e .

make pip-compile: pip-compile-app pip-compile-dev

pip-compile-app:
	@.virtualenv/bin/pip-compile --verbose --allow-unsafe --no-emit-trusted-host --upgrade --output-file requirements.txt requirements.in
	git diff --color=always --exit-code requirements.txt

pip-compile-dev:
	@.virtualenv/bin/pip-compile --verbose --allow-unsafe --no-emit-trusted-host --upgrade --output-file requirements-dev.txt requirements-dev.in
	git diff --color=always --exit-code requirements-dev.txt

nuke-pyc:
	@find zombie_labyrinth -name '*.pyc' -exec unlink '{}' \;

tasks:
	@echo 'clean                                    Delete temp files'
	@echo 'developer-setup                          Setup virtualenv and install dependencies'
	@echo 'pip-compile                              Update versions of python dependencies in requirements.txt'
