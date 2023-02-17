class FunctionWrapper:
    '''This class is used to create a "delayed" function,
    during initialization, the function itself and its arguments are passed'''
    def __init__(self, func, *args, **kwargs):
        self.func = func
        self.args = args
        self.kwargs = kwargs

    def do(self):
        self.func(*self.args, **self.kwargs)


class FunctionAnnotationInKv:
    def func_wrap(self, func, *args, **kwargs):
        return FunctionWrapper(func, *args, **kwargs)

    def function(self, *args, **kwargs):
        pass