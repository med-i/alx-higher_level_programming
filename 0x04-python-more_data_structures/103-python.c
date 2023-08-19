#include <Python.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);

/**
 *  print_python_list - prints some basic info about Python lists.
 * @p: PyObject
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t size = PyList_Size(p);
	Py_ssize_t allocated = ((PyListObject *)p)->allocated;
	Py_ssize_t i;
	PyObject *element;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", allocated);

	for (i = 0; i < size; i++)
	{
		element = ((PyListObject *)p)->ob_item[i];
		printf("Element %ld: ", i);

		if (PyBytes_Check(element))
		{
			printf("bytes\n");
			print_python_bytes(element);
		}
		else if (PyUnicode_Check(element))
			printf("str\n");
		else if (PyLong_Check(element))
			printf("int\n");
		else if (PyFloat_Check(element))
			printf("float\n");
		else if (PyTuple_Check(element))
			printf("tuple\n");
		else if (PyList_Check(element))
			printf("list\n");
	}
}

/**
 *  print_python_bytes - prints some basic info about Python bytes.
 * @p: PyObject
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t size, count, i;
	char *string;

	if (!PyBytes_Check(p))
	{
		printf("[.] bytes object info\n");
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = PyBytes_Size(p);
	string = PyBytes_AsString(p);

	printf("[.] bytes object info\n");
	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", string);

	count = size > 9 ? 10 : size + 1;
	printf("  first %ld bytes: ", count);
	for (i = 0; i < count; i++)
		printf("%02x ", (unsigned char)string[i]);
	printf("\n");
}
