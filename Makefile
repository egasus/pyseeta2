install: build.opencv3

build.opencv3:
	@USE_OPENCV3=ON python setup.py install

uninstall: clean
	@pip uninstall pyseeta2

preinstall:
	@if [ ! -f "models/fr_2_10.dat" ]; then cd models; unrar x fr_2_10.dat.part1.rar; fi

test: preinstall
	@python examples/det.py
