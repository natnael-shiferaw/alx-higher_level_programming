#include <stdio.h>
#include <Python.h>

/**
* print_python_bytes - USED TO PRINT BYTES INFORMATION.
*
* @p: IS A PYTHON OBJECT.
* Return: NOTHING.
*/

void print_python_bytes(PyObject *p)
{
	char *str;
	long int SIZE, j, lim;

	printf("[.] bytes object info\n");

	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	SIZE = ((PyVarObject *)(p))->ob_size;
	str = ((PyBytesObject *)p)->ob_sval;

	printf("  size: %ld\n", SIZE);
	printf("  trying string: %s\n", str);

	if (SIZE >= 10)
		lim = 10;
	else
		lim = SIZE + 1;

	printf("  first %ld bytes:", lim);

	for (j = 0; j < lim; j++)
		if (str[j] >= 0)
			printf(" %02x", str[j]);
		else
			printf(" %02x", 256 + str[j]);

	printf("\n");
}

/**
* print_python_list - USED TO PRINT LIST INFORMATION.
*
* @p: REPRESENTS A PYTHON OBJECT
* Return: NOTHING.
*/

void print_python_list(PyObject *p)
{
	long int SIZE, j;
	PyListObject *LIST;
	PyObject *OBJ;

	SIZE = ((PyVarObject *)(p))->ob_size;
	LIST = (PyListObject *)p;

	printf("[*] Python list info\n");

	printf("[*] Size of the Python List = %ld\n", SIZE);
	printf("[*] Allocated = %ld\n", LIST->allocated);

	for (j = 0; j < SIZE; j++)
	{
		OBJ = ((PyListObject *)p)->ob_item[j];
		printf("Element %ld: %s\n", j, ((OBJ)->ob_type)->tp_name);
		if (PyBytes_Check(OBJ))
			print_python_bytes(OBJ);
	}
