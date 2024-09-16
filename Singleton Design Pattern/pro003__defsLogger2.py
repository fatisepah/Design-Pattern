import pro002__defsLogger1


for i in range(10):
    pro002__defsLogger1.info("Info message {0}".format(i))
    pro002__defsLogger1.debug("Debug message {0}".format(i))
    pro002__defsLogger1.warning("Warning message {0}".format(i))
    pro002__defsLogger1.error("Error message {0}".format(i))
    pro002__defsLogger1.critical("Critical message {0}".format(i))