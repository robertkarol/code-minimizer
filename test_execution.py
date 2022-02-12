from unittest import main

def run_tests(module):
    test = main(module=module, exit=False)
    return test.result.wasSuccessful()

def try_run_tests(module):
    try:
        return run_tests(module)
    except (IndentationError, SyntaxError) as e:
        print(e)
        return False