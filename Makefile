

.SILENT: run
.PHONY: run




ifneq (,$(wildcard ./.local.env))
    include .local.env
    export
endif

run:
	python3 main.py

freeze:
	pip freeze > requirements.txt

app:
	python setup.py py2app -A


build:
	python setup.py py2app