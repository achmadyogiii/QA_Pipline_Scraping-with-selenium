import pandas as pd
import psycopg2

def load_data_to_postgres():
    print("🚀 Memulai proses load data dari CSV ke PostgreSQL...")

    # Membaca data dari file CSV
    df = pd.read_csv("data_buku_raw.csv")

    # kredensial database PostgreSQL
    conn = psycopg2.connect(
        host="localhost",
        database="db_qa_audit",
        user="postgres",
        password="Tradisional03!"  # Ganti dengan password PostgreSQL Anda
    )
    cursor = conn.cursor()

    # Memasukkan setiap baris data ke tabel 'products'
    for _, row in df.iterrows():
        cursor.execute(
            """
            INSERT INTO products (title, price_gbp, availability)
            VALUES (%s, %s, %s)
            """,
            (row['title'], row['price_gbp'], row['availability'])
        )

    conn.commit()
    cursor.close()
    conn.close()
    print(f"✅ Selesai! Berhasil memuat {len(df)} data ke tabel 'products' di PostgreSQL.\n")

if __name__ == "__main__":
    load_data_to_postgres()
