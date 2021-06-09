from app import index, getme


def test_index():
	assert index() == "Hello"

def test_getme():
	assert getme() == "getme"
