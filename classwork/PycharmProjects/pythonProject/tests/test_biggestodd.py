from unittest import TestCase
#from largest import biggest_odd
#from largest import equal_string

from pythonProject.largest import createDick


class MyTestBigOdd(TestCase):
   # def test_biggest_odd_function(self):
     #  self.assertEqual(biggest_odd("23956"), 9)

    #def test_if_two_string_are_equal(self):
       #self.assertEqual(equal_string("love", "evol"), True)
       # self.assertEqual(equal_string("self", "left"), False)

    def test_list_to_dick(self):
        self.assertEqual(createDick([1,2,3,4,5]), {1: 1, 2: 8, 3: 27, 4: 64, 5: 125})

