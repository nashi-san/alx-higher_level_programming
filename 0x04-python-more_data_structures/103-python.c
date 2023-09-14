#include <Python.h>
/**
 * print_python_bytes - Prints bytes information
 * @p: Python Object
 * Return: no return
 */
void print_python_bytes(PyObject *p)
{
        Py_ssize_t size, i;
        char *str;

        printf("[.] bytes object info\n");
        if (!PyBytes_Check(p))
        {
                printf("  [ERROR] Invalid Bytes Object\n");
                return;
        }
        size = PyBytes_GET_SIZE(p);                                                                                                                                     str = PyBytes_AS_STRING(p);
        printf("  size: %ld\n", size);
        printf("  trying string: %s\n", str);
        if (size > 10)
                size = 10;
        printf("  first %ld bytes: ", size);
        for (i = 0; i < size; i++)
        {
                printf("%02hhx", str[i]);
                if (i == size - 1)
                        printf("\n");
                else
                        printf(" ");
        }
}
/**
 * print_python_list - Prints list information
 * @p: Python Object
 * Return: no return
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t size, i;
	PyObject *item;

	size = PyList_Size(p);
	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);
	for (i = 0; i < size; i++)
	{
		item = ((PyListObject *)p)->ob_item[i];
		printf("Element %ld: %s\n", i, ((item)->ob_type)->tp_name);
		if (PyBytes_Check(item))
			print_python_bytes(item);
	}
}
