class Base(object):
    def __init__(self):
        print "Base created"

    def print_test(self):
        print "this is a test line"

class ChildA(Base):
    def __init__(self):
        print "\n\ninside of ChildA init"
        Base.__init__(self)
        #Base.print_test(self)

class ChildB(Base):
    def __init__(self):
        print "\n\ninside of ChildB init"
        super(ChildB, self).__init__()
        super(ChildB, self).print_test()
        self.print_test()

print ChildA(),ChildB()
