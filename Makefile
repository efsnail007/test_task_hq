lint:
	pylint --rcfile pylint.cfg src
	black --check --config black.toml src

format:
	black --verbose --config black.toml src 
	isort --sp .isort.cfg src
