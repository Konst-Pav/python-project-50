install:
	poetry install

gendiff:
	poetry run gendiff

gendiff-test:
	poetry run gendiff './tests/file_1.json' './tests/file_2.json'

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