install:
	poetry install

project:
	poetry rub project

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python -m pip install dist/labyrinth_game_ivanishchev_vitaly_m25_555-0.1.0-py3-none-any.whl

lint:
	poetry runn ruff check .
