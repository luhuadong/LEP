class SocketIOBlueprint:

    def __init__(self, io, namespace=None,  **kwargs):
        self.namespace = namespace or '/'
        self._handlers = []
        self.io = None

    def on(self, key):
        """ A decorator to add a handler to a blueprint. """
        def wrapper(f):
            if not callable(f):
                raise ValueError('handle must wrap a callable')
            def wrap(io):
                @io.on(key, namespace=self.namespace)
                def wrapped(*args, **kwargs):
                    return f(*args, **kwargs)
                return io
            self._handlers.append(wrap)
        return wrapper

    def init_io(self, io):
        self.io = io
        for f in self._handlers:
            f(io)

        return io

    def get_io(self):
        return self.io
