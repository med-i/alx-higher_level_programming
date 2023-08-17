#include <Python.h>

void print_python_list(PyObject *p)
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

void print_python_bytes(PyObject *p)
{
	Py_ssize_t size = PyBytes_Size(p), count, i;
	const char *string = PyBytes_AsString(p);

	printf("[.] bytes object info\n");
	printf("size: %ld\n", size);
	printf("trying string: %s\n", string);

	count = size > 9 ? 10 : size + 1;
	printf("First %ld bytes: ", count);
	for (i = 0; i < count; i++)
		printf("%02x ", (unsigned char)string[i]);
	printf("\n");
}

/*
[.] bytes object info
  size: 5
  trying string: Hello
  first 6 bytes: 48 65 6c 6c 6f 00
[.] bytes object info
  size: 8
  trying string: �
  first 9 bytes: ff f8 00 00 00 00 00 00 00
*/
