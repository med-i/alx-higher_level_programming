#!/usr/bin/python3
import ctypes

lib = ctypes.CDLL('./libPython.so')
lib.print_python_list.argtypes = [ctypes.py_object]
lib.print_python_bytes.argtypes = [ctypes.py_object]
b = b'aaa';
lib.print_python_bytes(b);
