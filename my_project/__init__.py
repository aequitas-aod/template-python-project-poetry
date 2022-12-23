import logging


logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('my_project')

# this is the initial module of your app
# this is executed whenever some client-code is calling `import my_project` or `from my_project import ...`
# put your main classes here, eg:
class MyClass:
    def my_method(self):
        return "Hello World"


# let this be the last line of this file
logger.info("my_project loaded")
