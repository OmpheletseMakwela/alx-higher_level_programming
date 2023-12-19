#include <Python.h>

void print_python_list(PyObject *p) {
    Py_ssize_t size, i;
    PyObject *element;

    if (!PyList_Check(p)) {
        printf("[ERROR] Invalid List Object\n");
        fflush(stdout);
        return;
    }

    size = PyList_Size(p);
    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %ld\n", size);

    printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);
    for (i = 0; i < size; ++i) {
        element = PyList_GetItem(p, i);
        printf("Element %ld: %s\n", i, Py_TYPE(element)->tp_name);
    }
    fflush(stdout);
}

void print_python_bytes(PyObject *p) {
    Py_ssize_t size, i;
    char *str;

    if (!PyBytes_Check(p)) {
        printf("[ERROR] Invalid Bytes Object\n");
        fflush(stdout);
        return;
    }

    size = PyBytes_Size(p);
    printf("[.] bytes object info\n");
    printf("  [.] Size: %ld\n", size);
    printf("  [.] trying string: %s\n", PyBytes_AsString(p));

    printf("  [.] first %ld bytes:", (size < 10) ? size : 10);
    str = PyBytes_AsString(p);
    for (i = 0; i < size && i < 10; ++i) {
        printf(" %02hhx", str[i]);
    }
    printf("\n");
    fflush(stdout);
}

void print_python_float(PyObject *p) {
    char *buffer;
    double value;

    if (!PyFloat_Check(p)) {
        printf("[ERROR] Invalid Float Object\n");
        fflush(stdout);
        return;
    }

    value = ((PyFloatObject *)p)->ob_fval;
    printf("[.] float object info\n");
    printf("  [.] value: %g\n", value);
    buffer = PyOS_double_to_string(value, 'r', 0, Py_DTSF_ADD_DOT_0, NULL);
    printf("  [.] precision: %d\n", (int)strlen(buffer) - 1);
    PyMem_Free(buffer);
    fflush(stdout);
}
