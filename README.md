# pyseeta2

A python API interface for [SeetaFace2](https://github.com/seetafaceengine/SeetaFace2)

## Installation
### PreInstall
```bash
sudo apt-get install libopencv-dev
sudo pip install opencv-contrib-python 
```
### [SeetaFace2](https://github.com/seetafaceengine/SeetaFace2)
``` bash
git clone https://github.com/seetafaceengine/SeetaFace2
cd SeetaFace2
mkdir build
cd build
cmake .. -DCMAKE_INSTALL_PREFIX=`pwd`/install -DCMAKE_BUILD_TYPE=Release -DBUILD_EXAMPLE=OFF # 如果有 OpenCV，则设置为 ON
cmake --build .  --config Release --target install
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:`pwd`/lib
```
### PySeeta2

``` bash
git clone --recursive https://github.com/gaojunying/pyseeta2
cd pyseeta2
sudo make setup
```
If you want to build with opencv3

``` bash
USE_OPENCV3=ON python setup.py build
```