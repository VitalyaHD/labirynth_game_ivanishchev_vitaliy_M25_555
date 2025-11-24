install:
	poetry install

project:
	poetry rub project

build:
	poetry puild

publish:
	poetry publish --dry-run

package-install:
	python -m pip install dist/*whl

lint:
	poetry runn ruff check .
