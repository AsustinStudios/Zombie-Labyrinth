SHELL := /bin/bash

current_dir = $(shell pwd)
PYTHON = /usr/bin/env PYTHONPATH=. $(shell pwd)/.virtualenv/bin/python

DEFAULT: tasks

clean: nuke-pyc

nuke-pyc:
	@find src -name '*.pyc' -exec unlink '{}' \;

tasks:
	@echo 'clean                                    Delete temp files'
