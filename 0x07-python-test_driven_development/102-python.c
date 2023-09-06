#include <Python.h>

/**
 * print_python_string - Print the basic info of a Python string object
 * @p: PyObject string
 */
void print_python_string(PyObject *p)
{
	Py_ssize_t length;
	const char *str_value;
	const char *type;

	if (!PyUnicode_Check(p))
	{
		printf("[.] string object info\n");
		printf("  [ERROR] Invalid String Object\n");
		return;
	}

	length = PyUnicode_GET_LENGTH(p);
	str_value = PyUnicode_AsUTF8(p);

	if (PyUnicode_IS_COMPACT_ASCII(p))
		type = "compact ascii";
	else
		type = "compact unicode object";

	printf("[.] string object info\n");
	printf("  type: %s\n", type);
	printf("  length: %ld\n", length);
	printf("  value: %s\n", str_value);
}
