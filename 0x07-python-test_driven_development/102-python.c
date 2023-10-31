#include "Python.h"


/**
 * print_python_string - A FUNCTION THAT IS USED TO PRINTS
 *  INFORMATION ABOUT PYTHON STRINGS.
 *
 * @p: REPRESENTS A PyObject WHICH IS A STRING OBJECT.
 */

void print_python_string(PyObject *p)
{
long int LEN;

fflush(stdout);

printf("[.] string object info\n");

if (strcmp(p->ob_type->tp_name, "str") != 0)
{
	printf("  [ERROR] Invalid String Object\n");
}

LEN = ((PyASCIIObject *)(p))->LEN;

if (PyUnicode_IS_COMPACT_ASCII(p))
	printf("  type: compact ascii\n");

else
	printf("  type: compact unicode object\n");

printf("  LEN: %ld\n", LEN);

printf("  value: %ls\n", PyUnicode_AsWideCharString(p, &LEN));
}
