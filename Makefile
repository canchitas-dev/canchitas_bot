lint:
	@flake8 --config=.flake8 /dev/null $(shell git diff --name-only HEAD | grep '\.py$$' )