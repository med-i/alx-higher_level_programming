#include <Python.h>
#include "stdio.h"

/**
 *  print_python_list_info - prints some basic info about Python lists.
 * @p: PyObject
 */
void print_python_list_info(PyObject *p)
{
	Py_ssize_t size = PyList_Size(p);
	Py_ssize_t allocated = ((PyListObject *)p)->allocated;
	Py_ssize_t i;
	PyObject *element, *type;

	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", allocated);

	for (i = 0; i < size; i++)
	{
		element = PyList_GetItem(p, i);
		type = PyObject_Type(element);

		printf("Element %ld: %s\n", i,
		       PyUnicode_AsUTF8(PyObject_GetAttrString(type, "__name__")));
	}
}
