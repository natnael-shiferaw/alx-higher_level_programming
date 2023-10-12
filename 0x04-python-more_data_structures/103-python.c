#define PY_SSIZE_T_CLEAN
#include <Python.h>


void print_python_bytes(PyObject *p);

/**
* print_python_list - USED TO PRINT INFO ABOUT PYTHON LISTS.
* @p: REPRESENTS PYOBJECT STRUCT.
*/

void print_python_list(PyObject *p)
{
	PyListObject *OBJ;
	PyVarObject *var_OBJ;
	PyObject *ITEM;
	Py_ssize_t j, SIZE, ALLOC;
	const char *TYPE;

	OBJ = (PyListObject *)p;
	var_OBJ = (PyVarObject *)p;

	SIZE = var_OBJ->ob_size;
	ALLOC = OBJ->allocated;

	printf("[*] Python list info\n");

	printf("[*] Size of the Python List = %zd\n", SIZE);
	printf("[*] Allocated = %zd\n", ALLOC);

	j = 0;
	while (j < SIZE)
	{
		ITEM = OBJ->ob_item[j];
		TYPE = ITEM->ob_type->tp_name;
		printf("Element %zd: %s\n", j++, TYPE);

		if (strcmp(TYPE, "bytes") == 0)
			print_python_bytes(ITEM);
	}
}

/**
* print_python_bytes - USED TO PRINT INFO ABOUT PYTHON BYTES
* @p: POINTER TO PYOBJECT STRUCT
*/

void print_python_bytes(PyObject *p)
{
	Py_ssize_t j, SIZE, Nbytes;
	PyBytesObject *OBJ;
	PyVarObject *var_OBJ;
	char *string;

	printf("[.] bytes object info\n");

	if (strcmp(p->ob_type->tp_name, "bytes"))
		printf("  [ERROR] Invalid Bytes Object\n");
	else
	{
		OBJ = (PyBytesObject *)p;
		var_OBJ = (PyVarObject *)p;
		SIZE = var_OBJ->ob_size;
		string = OBJ->ob_sval;
		Nbytes = SIZE >= 10 ? 10 : SIZE + 1;

		printf("  size: %zd\n", SIZE);
		printf("  trying string: %s\n", string);
		printf("  first %zd bytes: ", Nbytes);

		j = 0;
		while (j < Nbytes)
		{
			printf("%02hhx", string[j++]);
			if (j < Nbytes)
				printf(" ");
			else
				printf("\n");
		}
	}
}
