setup:
	@python setup.py install

uninstall: clean
	@pip uninstall pyseeta2

clean:
	@rm build/ dist/ -rf
	@rm build/ dist/ src/python_seetaface2.egg-info -rf