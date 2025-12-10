import sqlite3
import pandas as pd


def run_customer_spending_analysis():
    """
    Analyzing customer spending by joining customers, orders,
    order_items, and products tables.
    Printing top 5 customers by total amount spent.
    """

    db_path = "ecommerce.db"
    conn = sqlite3.connect(db_path)

    # Query to calculate total spending per customer
    sql_query = """
        SELECT
            c.name AS customer_name,
            c.email AS customer_email,
            COUNT(DISTINCT o.order_id) AS total_orders,
            ROUND(SUM(oi.quantity * oi.price_at_purchase), 2) AS total_spent
        FROM customers c
        JOIN orders o
            ON c.customer_id = o.customer_id
        JOIN order_items oi
            ON o.order_id = oi.order_id
        WHERE o.status != 'Cancelled'
        GROUP BY c.customer_id
        ORDER BY total_spent DESC
        LIMIT 5;
    """

    print("Running customer spending analysis...")

    try:
        result_df = pd.read_sql_query(sql_query, conn)

        print("\n--- Top 5 Customers by Total Spending ---")
        print(result_df.to_string(index=False))
    finally:
        # Closing the Connection 
        conn.close()


if __name__ == "__main__":
    run_customer_spending_analysis()
