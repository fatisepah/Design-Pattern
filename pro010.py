class SingletonObject(object):
    class _Logger():
    
        def __init__(self,filename):
            self.filename=filename

        def __str__(self):
            return "{0!r}{1}".format(self,self.filename)
        #if we use _ for the method name it will not be callable from outside like private methods
        def _write_log(self,level,msg):
            with open(self.filename,'a') as log_file:
                log_file.write("[{0}] {1}\n".format(level,msg))

        def critical(self,msg):
            self.write_log("CRITICAL",msg)

        def error(self,msg):
            self.write_log("ERROR",msg)

        def warning(self,msg):
            self.write_log("WARNING",msg)

        def info(self,msg):
            self.write_log("INFO",msg)

        def debug(self,msg):
            self.write_log("DEBUG",msg)
        
    instance=None

    def __new__(cls):
        if not SingletonObject.instance:
            SingletonObject.instance=SingletonObject.__SingletonObject()
        
        return SingletonObject.instance
    
    def __getattr__(self, name):
        return getattr(self.instance, name)
    def __setattr__(self, name):
        return setattr(self.instance, name) 
