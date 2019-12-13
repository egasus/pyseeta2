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

```
### PySeeta2

``` bash
git clone --recursive https://github.com/gaojunying/pyseeta2
cd pyseeta2

[SeetaFace2]
cd SeetaFace2
mkdir build
cd build
cmake .. -DCMAKE_INSTALL_PREFIX=`pwd`/install -DCMAKE_BUILD_TYPE=Release -DBUILD_EXAMPLE=OFF # 如果有 OpenCV，则设置为 ON
cmake --build .  --config Release --target install
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:`pwd`/lib
cd ..
cp build/bin/* ../lib/x64
cp -rf build/install/include ../src/
cp example/tracking/seeta/Struct_cv.h ../src/include/seeta
cd ..

[pybind11]
cd pybind11
git checkout tags/v2.4.3
cd ..

[install]
sudo make install
```

## Example
```bash
[detection]
python example/det.py
```
![Result](/example/example1_result.jpg)
```bash
[recognition]
python example/rec.py
```
## Thanks
- [@twmht](https://github.com/twmht/python-seetaface2)
