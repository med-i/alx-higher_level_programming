#!/usr/bin/python3
str = "Python is an interpreted, interactive, object-oriented programming\
 language that combines remarkable power with very clear syntax"
str = str.split(" ", 5)[5].split("language")[0] + "with Python"
print(str)
