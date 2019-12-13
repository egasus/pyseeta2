setup:
	@python setup.py install

setup.opencv3:
	@USE_OPENCV3=ON python setup.py install

uninstall: clean
	@pip uninstall pyseeta2

clean:
	@rm build/ dist/ -rf
	@rm build/ dist/ src/pyseeta2.egg-info -rf

rar.compress:
	@cd models; rar a -v40000k fr_2_10.dat.rar fr_2_10.dat

rar.extract:
	@unrar x fr_2_10.dat.part1.rar

test:
	@python example/det.py