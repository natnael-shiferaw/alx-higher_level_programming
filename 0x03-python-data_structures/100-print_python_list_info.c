#include <Python.h>

/**
* print_python_list_info - A FUNCTION THAT PRINTS A BASIC
*   INFORMATION ABOUT PYTHON LISTS.
* @p: REPRESENTS A PyObject LIST.
*/

void print_python_list_info(PyObject *p)
{
	int SIZE, ALLOC, j;
	PyObject *OBJ;

	SIZE = Py_SIZE(p);
	ALLOC = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", SIZE);
	printf("[*] Allocated = %d\n", ALLOC);

	for (j = 0; j < SIZE; j++)
	{
		printf("Element %d: ", j);

		OBJ = PyList_GetItem(p, j);
		printf("%s\n", Py_TYPE(OBJ)->tp_name);
	}
}
