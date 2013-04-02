import sys


class Func(object):

    def __init__(self, func, args, job):
        self.args = args
        self.job = job

        try:
            # If the function passed is an instance method,
            # set who called the function, the function itself, and the
            # function args
            self.caller = func.__self__
            self.name = func.__name__
        except AttributeError:
            # Function passed isn't an instance method
            self.func = func

    def execute(self):
        try:
            # If the function is an instance method, it will have the caller
            # set so we have to bind the method
            func = getattr(self.caller, self.name)
        except AttributeError:
            func = self.func

        try:
            # Execute the func then tell parent job that this func finished
            # successfully or if it failed
            func(*self.args)
            self.job.finished_successfully()
        except:
            self.job.failed(sys.exc_info()[0])