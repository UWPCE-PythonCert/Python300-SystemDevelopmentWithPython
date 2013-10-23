#include <Python.h>

static PyObject *
divide(PyObject *self, PyObject *args)
{
    double x;
    double y;
    double sts;

    if (!PyArg_ParseTuple(args, "dd", &x, &y))
        return NULL;
    if (y == 0) {
        PyErr_SetString(PyExc_ZeroDivisionError, "DIVIDE BY ZERO ERROR");
        return NULL;
    }
    sts = x/y;
    return Py_BuildValue("d", sts);
}

// Module's method table and initialization function
// See: http://docs.python.org/extending/extending.html#the-module-s-method-table-and-initialization-function
static PyMethodDef DivideMethods[] = {
    {"divide", divide, METH_VARARGS, "divide two numbers"},
    {NULL, NULL, 0, NULL}
};

void initdivide(void) {
    // Module's initialization function
    // Will be called again if you use Python's reload()

    PyImport_AddModule("divide");
    Py_InitModule("divide", DivideMethods);
}

int main(int argc, char *argv[]) {
    Py_SetProgramName(argv[0]);

    Py_Initialize();

    initdivide();

    return 0;
}
