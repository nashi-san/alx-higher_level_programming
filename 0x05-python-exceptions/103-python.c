#include <Python.h>
#include <stdio.h>

void print_python_list(PyObject *p)
{
	PyListObject *list = (PyListObject *)p;
	Py_ssize_t size = PyList_Size(p);
	Py_ssize_t i;
	PyObject *item;
	const char *type;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", list->allocated);
	for (i = 0; i < size; i++)
	{
		item = PyList_GetItem(p, i);
		type = Py_TYPE(item)->tp_name;
		printf("Element %ld: %s\n", i, type);
	}
}
void print_python_bytes(PyObject *p)
{
	PyBytesObject *bytes = (PyBytesObject *)p;
	Py_ssize_t size = PyBytes_Size(p);
	Py_ssize_t i;

	printf("[.] bytes object info\n");
	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", bytes->ob_sval);
	printf("  first %ld bytes: ", (size < 10) ? size + 1 : 10);
	for (i = 0; i < size && i < 10; i++)
	{
		printf("%02x", bytes->ob_sval[i] & 0xff);
		if (i == 9 && size >= 10)
			printf("...");
	}
	printf("\n");
}
void print_python_float(PyObject *p)
{
	PyFloatObject *f = (PyFloatObject *)p;
	double value = f->ob_fval;

	printf("[.] float object info\n");
	if (!PyFloat_Check(p))
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}
	printf("  value: %.*g\n", 16, value);
}
