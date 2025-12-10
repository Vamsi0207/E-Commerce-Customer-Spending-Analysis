import os
import sqlite3

import pandas as pd


def ingest_data() :
   

    db_path = "ecommerce.db"

    # Connect to SQLite database (creates the file if it doesn't exist)
    conn = sqlite3.connect(db_path)

    # Map table names to their corresponding CSV file paths
    csv_files = {
        "customers": "data/customers.csv",
        "products": "data/products.csv",
        "orders": "data/orders.csv",
        "order_items": "data/order_items.csv",
        "payments": "data/payments.csv",
    }

    print("Starting data ingestion...")

    try:
        for table_name, file_path in csv_files.items():
            #If file does not exist in Folder then skip it
            if not os.path.exists(file_path):
                print(f"  [!] Skipping '{table_name}': file not found at {file_path}")
                continue

            # Read CSV into a DataFrame
            df = pd.read_csv(file_path)

            # Write DataFrame to a table in SQLite.
            # if_exists='replace' will drop the table if it already exists.
            df.to_sql(table_name, conn, if_exists="replace", index=False)

            print(f" ->Table '{table_name}' created with {len(df)} rows.")

        print(f"Data ingestion complete. Database '{db_path}' is ready.")
    finally:
        # Closing the Connection after Ingestion is Done
        conn.close()


if __name__ == "__main__":
    ingest_data()
