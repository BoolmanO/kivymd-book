class FunctionWrapper:
    '''This class is used to create a "delayed" function,
    during initialization, the function itself and its arguments are passed'''
    def __init__(self, func, *args, **kwargs):
        self.func = func
        self.args = args
        self.kwargs = kwargs

    def do(self):
        return self.func(*self.args, **self.kwargs)


def func_wrap(self, func, *args, **kwargs) -> FunctionWrapper:
    return FunctionWrapper(func, *args, **kwargs)