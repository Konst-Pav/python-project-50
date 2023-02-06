install:
	poetry install

gendiff:
	poetry run gendiff

gendiff-test:
	poetry run gendiff '/home/konstantin/projects/python-project-50/tests/file_1.json' '/home/konstantin/projects/python-project-50/tests/file_2.json'

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

package-reinstall:
	python3 -m pip install --user --force-reinstall dist/*.whl

lint:
	poetry run flake8 hexlet_code

pytest:
	poetry run pytest