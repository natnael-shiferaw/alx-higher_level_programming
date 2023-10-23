#include <Python.h>
#include <stdio.h>

/**
* print_python_float - PROVIDES INFO ON the PyFloatObject
* @p: REPRESENTS the PyObject
*/

void print_python_float(PyObject *p)
{
	char *STR = NULL;
	double VAL = 0;

	fflush(stdout);
	printf("[.] float object info\n");

	if (!PyFloat_CheckExact(p))
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}

	VAL = ((PyFloatObject *)p)->ob_fval;
	STR = PyOS_double_to_string(VAL, 'r', 0, Py_DTSF_ADD_DOT_0, NULL);
	printf("  value: %s\n", STR);
}

/**
* print_python_bytes - PROVIDES INFO ON the PyBytesObject
* @p: REPRESENTS the PyObject
*/

void print_python_bytes(PyObject *p)
{
	char *STR = NULL;
	Py_ssize_t SIZE = 0, K = 0;

	fflush(stdout);
	printf("[.] bytes object info\n");
	if (!PyBytes_CheckExact(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	SIZE = PyBytes_Size(p);
	printf("  size: %zd\n", SIZE);
	STR = (assert(PyBytes_Check(p)), (((PyBytesObject *)(p))->ob_sval));
	printf("  trying string: %s\n", STR);
	printf("  first %zd bytes:", SIZE < 10 ? SIZE + 1 : 10);

	while (K < SIZE + 1 && K < 10)
	{
		printf(" %02hhx", STR[K]);
		K++;
	}
	printf("\n");
}

/**
* print_python_list - PROVIDES INFO ON the PyListObject
* @p: REPRESENTS the PyObject
*/

void print_python_list(PyObject *p)
{
	int K = 0;
	PyObject *ITEM;
	Py_ssize_t SIZE = 0;

	fflush(stdout);
	printf("[*] Python list info\n");

	if (PyList_CheckExact(p))
	{
		SIZE = PyList_GET_SIZE(p);
		printf("[*] Size of the Python List = %zd\n", SIZE);
		printf("[*] Allocated = %lu\n", ((PyListObject *)p)->allocated);
		while (K < SIZE)
		{
			ITEM = PyList_GET_ITEM(p, K);
			printf("Element %d: %s\n", K, ITEM->ob_type->tp_name);
			if (PyBytes_Check(ITEM))
				print_python_bytes(ITEM);
			else if (PyFloat_Check(ITEM))
				print_python_float(ITEM);
			K++;
		}
	}

	else
		printf("  [ERROR] Invalid List Object\n");
}
