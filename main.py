import pandas as pd

def load_data(file_path):
    return pd.read_csv(file_path)

def calculate_monthly_revenue(df):
    df['order_date'] = pd.to_datetime(df['order_date'])
    df['month'] = df['order_date'].dt.to_period('M')
    df['total_revenue'] = df['product_price'] * df['quantity']
    monthly_revenue = df.groupby('month')['total_revenue'].sum().reset_index()
    return monthly_revenue

def calculate_product_revenue(df):
    df['total_revenue'] = df['product_price'] * df['quantity']
    product_revenue = df.groupby(['product_id', 'product_name'])['total_revenue'].sum().reset_index()
    return product_revenue

def calculate_customer_revenue(df):
    df['total_revenue'] = df['product_price'] * df['quantity']
    customer_revenue = df.groupby('customer_id')['total_revenue'].sum().reset_index()
    return customer_revenue

def top_10_customers_by_revenue(df):
    customer_revenue = calculate_customer_revenue(df)
    top_customers = customer_revenue.sort_values(by='total_revenue', ascending=False).head(10)
    return top_customers

if __name__ == '__main__':
    df = load_data('orders.csv')
    
    print("Monthly Revenue:")
    print(calculate_monthly_revenue(df))
    
    print("\nProduct Revenue:")
    print(calculate_product_revenue(df))
    
    print("\nCustomer Revenue:")
    print(calculate_customer_revenue(df))
    
    print("\nTop 10 Customers by Revenue:")
    print(top_10_customers_by_revenue(df))
