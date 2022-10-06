.PHONY: check clean install

CHECK_FILES = *.py

check:
	black $(CHECK_FILES)
	mypy --ignore-missing-imports --follow-imports skip $(CHECK_FILES)
	pylint $(CHECK_FILES)

clean:
	rm -rf .coverage.*

install:
	pip3 install --user coverage mypy pylint pytest

test: clean
	coverage run -m pytest -v -s \
		test_*.py
	coverage combine
	coverage report
	coverage html
