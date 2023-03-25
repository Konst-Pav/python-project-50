install:
	poetry install

gendiff:
	poetry run gendiff

gendiff-test-plain:
	poetry run gendiff -f 'plain' './tests/fixtures/nested_struct_1.json' './tests/fixtures/nested_struct_2.json'

gendiff-test-stylish:
	poetry run gendiff -f 'stylish' './tests/fixtures/nested_struct_1.json' './tests/fixtures/nested_struct_2.json'

gendiff-test-json:
	poetry run gendiff -f 'json' './tests/fixtures/nested_struct_1.json' './tests/fixtures/nested_struct_2.json'

gendiff-test-default:
	poetry run gendiff './tests/fixtures/nested_struct_1.json' './tests/fixtures/nested_struct_2.json'

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

package-reinstall:
	python3 -m pip install --user --force-reinstall dist/*.whl

lint:
	poetry run flake8 gendiff

pytest:
	poetry run pytest -vv

test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml