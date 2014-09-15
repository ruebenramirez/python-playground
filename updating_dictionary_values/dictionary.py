import testtools

class TestUpdatingPythonDictionaries(testtools.TestCase):
    def setUp(self):
        super(TestUpdatingPythonDictionaries, self).setUp()
        self.foo = {'a': False, 'b': False, 'c': False}

    def tearDown(self):
        super(TestUpdatingPythonDictionaries, self).tearDown()

    def test_updating_dictionary_values_manually(self):
        """
        I expect this doesn't work
        """
        for key, value in self.foo.iteritems():
            value = True
        
        for key, value in self.foo.iteritems():
            self.assertFalse(value)
    
    def test_updating_dictionary_keys_with_update_method(self):
        """
        I expect this is the python way of updating dictionary values.
        """

        dict_len = len(self.foo)
        for key, value in self.foo.iteritems():
            self.foo.update({key: True})
        
        self.assertEquals(dict_len, len(self.foo))
        
        for key, value in self.foo.iteritems():
            self.assertTrue(value)

        #for key, value in self.foo.iteritems():
        #    print "%s + %s" % (str(key), str(value))
