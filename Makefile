install:
	poetry install

gendiff:
	poetry run gendiff

gendiff-test-json:
	poetry run gendiff './tests/fixtures/file_1.json' './tests/fixtures/file_2.json'

gendiff-test-yaml:
	poetry run gendiff './tests/fixtures/file_1.yml' './tests/fixtures/file_2.yml'

gendiff-test-json-yaml:
	poetry run gendiff './tests/fixtures/file_1.json' './tests/fixtures/file_2.yml'

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

package-reinstall:
	python3 -m pip install --user --force-reinstall dist/*.whl

lint:
	poetry run flake8 gendiff_util

pytest:
	poetry run pytest -vv

test-coverage:
	poetry run pytest --cov=gen-diff-utility --cov-report xml