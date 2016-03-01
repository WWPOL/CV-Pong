class Enum(set):
    def __getattr__(self, name):
        if name in self:
            return name
        raise AttributeError

def log(message, log_class, log_level):
    """Log information to the console.
    If you are angry about having to use Enums instead of typing the classes and levels in, look up how any logging facility works.

    Arguments:
    message -- the relevant information to be logged
    log_class -- the category of information to be logged. Must be within util.log.LogClass
    log_level -- the severity of the information being logged. Must be within util.log.LogLevel
    """

    assert log_class in LogClass
    assert log_level in LogLevel

    print("%s/%s: %s" % (log_level, log_class, message))

LogClass = Enum(["CV", "GRAPHICS", "GENERAL"])
LogLevel = Enum(["VERBOSE", "INFO", "WARNING", "ERROR"])
