install: build.opencv3

build:
	@python setup.py build

build.opencv3:
	@USE_OPENCV3=ON python setup.py install

uninstall: clean
	@pip uninstall pyseeta2

clean:
	@rm build/ dist/ -rf
	@rm build/ dist/ src/pyseeta2.egg-info -rf
	@if [ -f "models/fr_2_10.dat" ]; then rm models/fr_2_10.dat; fi

rar.compress:
	@cd models; rar a -v40000k fr_2_10.dat.rar fr_2_10.dat

rar.extract:
	@cd models; unrar x fr_2_10.dat.part1.rar

test:
	@python example/det.py

commit: clean
	@if [ -d "pybind11" ]; then rm -rf pybind11 && mkdir pybind11; fi
	@if [ -d "SeetaFace2" ]; then rm -rf SeetaFace2 && mkdir SeetaFace2; fi
	@commit