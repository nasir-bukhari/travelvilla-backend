# Import the Add function, and assert that it works correctly.
from main import Add
from main import Mul


def TestAdd():
    assert Add(2, 3) == 5
    print("Add Function works correctly")


def TestMul():
    assert Mul(2, 3) == 6
    print("Add Function works correctly")


if __name__ == '__main__':
    TestAdd()
    TestMul()
