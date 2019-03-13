class Script:

    def __init__(self, script, user=None):
        self._script = script
        self._user = user
        self._kwargs = {}

    def __repr__(self):
        return "%s(%s), %s" % (
            self._script.__name__,
            ''.join(["%s=%s" % (str(k), str(v)) for k, v in self._kwargs]),
            self._user
        )

    def __call__(self, **kwargs):
        self._kwargs = kwargs
        return self._script(**kwargs)

    def name(self):
        return self._script.__name__

    def user(self):
        return self._user

    def kwargs(self):
        return self._kwargs
