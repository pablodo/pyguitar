from unittest import TestLoader

def suite():   
    loader = TestLoader()
    return loader.discover("pyguitar.apps.guitar.tests", pattern="*.py")
