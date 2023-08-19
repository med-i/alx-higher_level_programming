#!/usr/bin/python3
import ctypes

lib = ctypes.CDLL("./libPython.so")
lib.print_python_list.argtypes = [ctypes.py_object]
lib.print_python_bytes.argtypes = [ctypes.py_object]
b = b"What does the 'b' character do in front of a string literal?"
lib.print_python_bytes(b)
