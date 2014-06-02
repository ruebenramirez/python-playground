
class Foo(object):
    def __init__(self, bar):
        self.bar = bar 

import testtools
class TestPythonAnyFunction(testtools.TestCase):

    def setUp(self):
        super(TestPythonAnyFunction, self).setUp()
        self.tri1 = Foo(1)
        self.tri2 = Foo(2)
        self.tri3 = Foo(3)
        self.tri4 = Foo(4)

        self.my_tris = [self.tri1, self.tri2, self.tri3]

    def tearDown(self):
        super(TestPythonAnyFunction, self).tearDown()

    def test_find_correct_objects_with_the_any_python_method(self):
        tri1_found = any(self.tri1 == t for t in self.my_tris)
        self.assertTrue(tri1_found)

        tri2_found = any(self.tri2 == t for t in self.my_tris)
        self.assertTrue(tri2_found)

        tri3_found = any(self.tri3 == t for t in self.my_tris)
        self.assertTrue(tri3_found)

        # tri4 is not in the list and should be false on lookup
        tri4_found = any(self.tri4 == t for t in self.my_tris)
        self.assertFalse(tri4_found)

