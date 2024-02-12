#include <Python.h>
#include <stdio.h>
/**
 * print_python_list - Prints information about a Python list
 * @p: Pointer to the Python list object
 * Return: No return
 */
void print_python_list(PyObject *p)
{
	PyListObject *list;
	Py_ssize_t size, i;
	PyObject *item;
	const char *type;

	if (!PyList_Check(p))
	{
		printf("[ERROR] Invalid List Object\n");
		return;
	}

	list = (PyListObject *)p;
	size = PyList_Size(p);
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
/**
 * print_python_bytes - Prints information about a Python bytes object
 * @p: Pointer to the Python bytes object
 * Return: No return
 */
void print_python_bytes(PyObject *p)
{
	PyBytesObject *bytes;
	Py_ssize_t size, i;
	const char *string;

	if (!PyBytes_Check(p))
	{
		printf("[ERROR] Invalid Bytes Object\n");
		return;
	}
	bytes = (PyBytesObject *)p;
	size = PyBytes_Size(p);
	string = bytes->ob_sval;
	printf("[.] bytes object info\n");
	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", string);
	printf("  first %ld bytes: ", (size < 10) ? size + 1 : 10);
	for (i = 0; i < size && i < 10; i++)
	{
		printf("%02x", string[i] & 0xff);
		if (i == 9 && size >= 10)
			printf("...");
	}
	printf("\n");
}
/**
 * print_python_float - Prints information about a Python float object
 * @p: Pointer to the Python float object
 * Return: No return
 */
void print_python_float(PyObject *p)
{
	PyFloatObject *f;
	double value;

	if (!PyFloat_Check(p))
	{
		printf("[ERROR] Invalid Float Object\n");
		return;
	}
	f = (PyFloatObject *)p;
	value = f->ob_fval;
	printf("[.] float object info\n");
	printf("  value: %f\n", value);
}
