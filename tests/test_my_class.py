import pytest

from my_project import MyClass


# can test using classes, name must begin with `Test`
class TestMyClass:

    # test methods' names must begin with `test_`
    def test_my_method(self):
        x = MyClass().my_method()
        assert "Hello World" == x


# can also have standalone test functions, name must begin with `test_`
def test_sum():
    assert 1 + 2 == pytest.approx(3)

@pytest.fixture
def sample_fixture():
    return [42]

def test_sample_fixture(sample_fixture):
    assert sample_fixture == [42]
    sample_fixture.append(43)
    assert sample_fixture == [42, 43]

def test_sample_fixture_isolated(sample_fixture):
    assert sample_fixture == [42]