import pro002

for i in range(10):
    pro002.info("Info message {0}".format(i))
    pro002.debug("Debug message {0}".format(i))
    pro002.warning("Warning message {0}".format(i))
    pro002.error("Error message {0}".format(i))
    pro002.critical("Critical message {0}".format(i))