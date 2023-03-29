

.SILENT: run
.PHONY: run

run:
	python3 main.py

freeze:
	pip freeze > requirements.txt

app:
	python setup.py py2app -A


build:
	python setup.py py2app