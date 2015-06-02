test:
	nosetests

lint:
	pep8 acw tests
	pylint acw
