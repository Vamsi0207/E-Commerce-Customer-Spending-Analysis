import pandas as pd
import random
from faker import Faker
import os

# Initialize Faker and fix the seed so data is repeatable
fake = Faker()
Faker.seed(42)
random.seed(42)

# -----------------------------
# Defining number of Customers, Products, Orders
# -----------------------------
TOTAL_CUSTOMERS = 30
TOTAL_PRODUCTS = 30
TOTAL_ORDERS = 30


def generate_data():

    # -----------------------------
    # 1. Generating Customers data
    # -----------------------------
    # Customer Data contains customer_id, name, email, country, signup_date
    customer_records = []

    for customer_id in range(1, TOTAL_CUSTOMERS + 1):
        customer_records.append({
            "customer_id": customer_id,
            "name": fake.name(),
            "email": fake.email(),
            "country": fake.country(),
            "signup_date": fake.date_this_decade(),
        })

    customers_df = pd.DataFrame(customer_records)

    # -----------------------------
    # 2. Generating Products data
    # -----------------------------
    #Let us Define five Dummy categories of Products
    product_categories = ["Electronics", "Books", "Clothing", "Home", "Toys"] 
    product_records = []

    # Product Data contains product_id, product_name, category, price
    for product_id in range(1, TOTAL_PRODUCTS + 1):
        product_records.append({
            "product_id": product_id,
            "product_name": f"{fake.word().capitalize()} {fake.word().capitalize()}",
            "category": random.choice(product_categories),
            "price": round(random.uniform(10.0, 500.0), 2),
        })

    products_df = pd.DataFrame(product_records)

    # -----------------------------
    # 3. Generating Orders data
    # -----------------------------
    order_records = []

    # Orders Data contains order_id, customer_id, order_date, status of order
    for order_id in range(1, TOTAL_ORDERS + 1):
        order_records.append({
            "order_id": order_id,
            "customer_id": random.randint(1, TOTAL_CUSTOMERS),
            "order_date": fake.date_between(start_date="-1y", end_date="today"),
            "status": random.choice(["Pending", "Shipped", "Delivered", "Cancelled"]),
        })

    orders_df = pd.DataFrame(order_records)

    # -----------------------------
    # 4. Generating Order Items data
    #    (products inside each order)
    # -----------------------------
    order_item_records = []
    next_item_id = 1

    for order in order_records:
        # Each order can have between 1 and 5 different products
        number_of_items = random.randint(1, 5)

        for _ in range(number_of_items):
            selected_product = random.choice(product_records)
            quantity_purchased = random.randint(1, 3)

            order_item_records.append({
                "item_id": next_item_id,
                "order_id": order["order_id"],
                "product_id": selected_product["product_id"],
                "quantity": quantity_purchased,
                # Store price at purchase time in case prices change later
                "price_at_purchase": selected_product["price"],
            })

            next_item_id += 1

    order_items_df = pd.DataFrame(order_item_records)

    # -----------------------------
    # 5. Generating Payments data
    # -----------------------------
    payment_records = []
    next_payment_id = 1

    #Payments Data contains payment_id, order_id, amount, payment_method, payment_date
    for order in order_records:
        # Cancelled orders do not have payments
        if order["status"] == "Cancelled":
            continue

        # Calculate total amount for the order
        order_total_amount = sum(
            item["quantity"] * item["price_at_purchase"]
            for item in order_item_records
            if item["order_id"] == order["order_id"]
        )

        payment_records.append({
            "payment_id": next_payment_id,
            "order_id": order["order_id"],
            "amount": round(order_total_amount, 2),
            "payment_method": random.choice(
                ["Credit Card", "PayPal", "Bank Transfer"]
            ),
            "payment_date": order["order_date"],
        })

        next_payment_id += 1

    payments_df = pd.DataFrame(payment_records)

    # -----------------------------
    # Saving all datasets to CSV Format in data Folder
    # -----------------------------
    os.makedirs("data", exist_ok=True)

    customers_df.to_csv("data/customers.csv", index=False)
    products_df.to_csv("data/products.csv", index=False)
    orders_df.to_csv("data/orders.csv", index=False)
    order_items_df.to_csv("data/order_items.csv", index=False)
    payments_df.to_csv("data/payments.csv", index=False)

    print("Successfully generated 5 CSV files in the 'data' folder.")


if __name__ == "__main__":
    generate_data()
