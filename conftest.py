import pytest
import tempfile
import os

@pytest.fixture()
def cleandir():
    print('hihi')
    newpath = tempfile.mkdtemp()
    os.chdir(newpath)
    return 100
