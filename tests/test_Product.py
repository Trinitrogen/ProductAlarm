import unittest
from product import Product

class TestProduct(unittest.TestCase):
    def test_baseline_test(self):
        '''Baseline Test to make sure testing is evening functioning'''
        #Arrange
        #Act
        #Assert
        self.assertEqual(3,3)

    def test_product_creation(self):
        ''' Test If A Product Object Can Be Created '''
        test_product = Product.Product('Name','URL', 'Contacts')
        print(test_product.name)
        self.assertEqual(test_product.name,'Name')
        self.assertEqual(test_product.urls, 'URL')
        self.assertEqual(test_product.contacts, 'Contacts')


if __name__ == '___main___':
    unittest.main()