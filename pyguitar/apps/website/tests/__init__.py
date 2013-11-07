from unittest import TestLoader

def suite():   
    loader = TestLoader()
    return loader.discover("pyguitar.apps.website.tests", pattern="*.py")
