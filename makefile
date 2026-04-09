PYTHON = python3

run:
	$(PYTHON) app.py

install:
	pip3 install -r requirements.txt

freeze:
	pip3 freeze > requirements.txt

clean:
	find . -type d -name "__pycache__" -exec rm -r {} +

.PHONY: run install freeze clean