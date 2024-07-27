import unittest
import pandas as pd
from main import load_data, calculate_monthly_revenue, calculate_product_revenue, calculate_customer_revenue, top_10_customers_by_revenue

class TestOrderAnalysis(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.df = load_data('orders.csv')
        cls.df['order_date'] = pd.to_datetime(cls.df['order_date'])
        cls.df['month'] = cls.df['order_date'].dt.to_period('M')
        cls.df['total_revenue'] = cls.df['product_price'] * cls.df['quantity']

    def test_monthly_revenue(self):
        monthly_revenue = calculate_monthly_revenue(self.df)
        self.assertTrue(len(monthly_revenue) > 0)

    def test_product_revenue(self):
        product_revenue = calculate_product_revenue(self.df)
        self.assertTrue(len(product_revenue) > 0)

    def test_customer_revenue(self):
        customer_revenue = calculate_customer_revenue(self.df)
        self.assertTrue(len(customer_revenue) > 0)

    def test_top_10_customers(self):
        top_customers = top_10_customers_by_revenue(self.df)
        self.assertTrue(len(top_customers) <= 10)

if __name__ == '__main__':
    unittest.main()
