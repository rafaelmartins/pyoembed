import os


def get_fixture(filename):
    cwd = os.path.dirname(os.path.abspath(__file__))
    fixture = os.path.join(cwd, 'fixtures', filename)
    with open(fixture) as fp:
        return fp.read()
