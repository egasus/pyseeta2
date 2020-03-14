cmake_minimum_required(VERSION 2.8.12)
project(python_cpp_example)

option(USE_OPENCV3 ON)

SET(OPENCV_LIBS  opencv_core opencv_highgui opencv_imgproc)

if (USE_OPENCV3)
  SET(OPENCV_LIBS  ${OPENCV_LIBS} opencv_imgcodecs)
endif()

SET(SOURCE_DIR "src/api")
include_directories(${SOURCE_DIR})
include_directories(pybind11)
add_subdirectory(pybind11)

include_directories(src/include)

add_library(seeta_face_detector SHARED IMPORTED)
add_library(seeta_face_landmarker SHARED IMPORTED)
add_library(seeta_face_recognizer SHARED IMPORTED)
add_library(seeta_face_tracker SHARED IMPORTED)
add_library(seeta_face_net SHARED IMPORTED)
set_target_properties(seeta_face_detector PROPERTIES IMPORTED_LOCATION ${CMAKE_CURRENT_SOURCE_DIR}/lib/x64/libSeetaFaceDetector.so)
set_target_properties(seeta_face_landmarker PROPERTIES IMPORTED_LOCATION ${CMAKE_CURRENT_SOURCE_DIR}/lib/x64/libSeetaFaceLandmarker.so)
set_target_properties(seeta_face_recognizer PROPERTIES IMPORTED_LOCATION ${CMAKE_CURRENT_SOURCE_DIR}/lib/x64/libSeetaFaceRecognizer.so)
set_target_properties(seeta_face_tracker PROPERTIES IMPORTED_LOCATION ${CMAKE_CURRENT_SOURCE_DIR}/lib/x64/libSeetaFaceTracker.so)
set_target_properties(seeta_face_net PROPERTIES IMPORTED_LOCATION ${CMAKE_CURRENT_SOURCE_DIR}/lib/x64/libSeetaNet.so)


SET ( CMAKE_CXX_FLAGS "-std=c++11")
pybind11_add_module(seetaface ${SOURCE_DIR}/seetaface.cpp ${SOURCE_DIR}/ndarray_converter.cpp)
# target_link_libraries(seetaface PRIVATE seeta_face_cropper seeta_face_detector seeta_point_detector opencv_core opencv_highgui opencv_imgproc opencv_imgcodecs)
target_link_libraries(seetaface PRIVATE seeta_face_detector seeta_face_landmarker seeta_face_recognizer seeta_face_tracker seeta_face_net ${OPENCV_LIBS})
# target_link_libraries(seetaface PRIVATE seeta_face_detector ${OPENCV_LIBS})
