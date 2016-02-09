import datetime


class Session(object):
    def new_session(self):
        def __enter__(self):
                start = datetime.datetime.now()
        def __exit__(self, exc_type, exc_val, exc_tb):
            finish = datetime.datetime.now()
        total = (finish - start)