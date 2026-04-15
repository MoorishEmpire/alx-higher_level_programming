#include <Python.h>

void    print_python_list_info(PyObject *p)
{
    PyListObject   *list;
    Py_ssize_t      size;
    Py_ssize_t      i;

    list = (PyListObject *)p;
    size = PyList_GET_SIZE(p);

    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", list->allocated);

    i = 0;
    while (i < size)
    {
        printf("Element %ld: %s\n", i, Py_TYPE(list->ob_item[i])->tp_name);
        i++;
    }
}