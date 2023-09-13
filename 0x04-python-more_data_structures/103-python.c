#include <Python.h>
/**
 * print_python_list - Prints list information
 * @p: Python Object
 * Return: no return
 */

void print_python_list(PyObject *p)
{
	Py_ssize_t size = PyList_Size(p);
	Py_ssize_t i;
	PyObject *item;
	const char *item_type;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);
	for (i = 0; i < size; i++)
	{
		item = PyList_GetItem(p, i);
		item_type = Py_TYPE(item)->tp_name;
		printf("Element %ld: %s\n", i, item_type);
	}
}

/**
 * print_python_bytes - Prints bytes information
 * @p: Python Object
 * Return: no return
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t size;
	Py_ssize_t i;
	char *str;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	printf("  size: %ld\n", PyBytes_Size(p));
	printf("  trying string: %s\n", ((PyBytesObject *)p)->ob_sval);
	size = PyBytes_Size(p);
	str = ((PyBytesObject *)p)->ob_sval;
	printf("  first %ld bytes: ", size + 1 > 10 ? 10 : size + 1);
	for (i = 0; i < (size + 1 > 10 ? 10 : size + 1); i++)
	{
		printf("%02hhx", str[i]);
		if (i < 9 && i < size)
			printf(" ");
	}
	printf("\n");
}
