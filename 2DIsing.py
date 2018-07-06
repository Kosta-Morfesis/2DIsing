#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  6 13:38:18 2018

@author: kosta
"""

import unittest
import numpy as np

class TestSpinFlip(unittest.TestCase):
    
    def setUp(self):
        self.spin_old=0
        self.spin_new=spinflip(self.spin_old)
    
    def test_spin_flip(self):
        self.assertEqual(self.spin_new, abs(self.spin_old - 1), 'Spin did not flip!')

#class TestMakeLattice(unittest.TestCase):
#    def setUp(self):
#        self.




# spin = {0, 1}
def spinflip(spin):
    return abs(spin - 1)



if __name__=='__main__':
    
#    
#    suite = unittest.TestLoader().loadTestsFromTestCase(TestSpinFlip)
#    unittest.TextTestRunner(verbosity=2).run(suite)
    unittest.main()





