import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager

def jalankan_scraper_edge(jumlah_halaman=50):
    print("Memulai proses scraping data buku dari microsoft edge")

    #mengatur browser edge(headless = berjalan dilatar belakang)
    options = EdgeOptions()
    options.add_argument("--headless")  # Menjalankan browser dalam mode headless (tanpa GUI)

    #instalasi webdriver untuk microsoft edge
    driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()),
                            options=options
                            )
    data_buku = []

    #loop pengambilan data
    for page in range(1, jumlah_halaman + 1):
        url = f"https://books.toscrape.com/catalogue/page-{page}.html"
        driver.get(url)
        time.sleep(2)  # Memberikan jeda agar halaman dapat dimuat sepenuhnya

        elements = driver.find_elements(By.CLASS_NAME, "product_pod")
        for buku in elements:
            try:
                judul = buku.find_element(By.TAG_NAME, "h3").find_element(By.TAG_NAME, "a").get_attribute("title")
                harga_text = buku.find_element(By.CLASS_NAME, "price_color").text
                stock = buku.find_element(By.CLASS_NAME, "instock").text.strip()

                #format harga ke bentuk float
                harga = float(harga_text.replace("£", "").replace("Â", ""))

                data_buku.append({
                    "title": judul,
                    "price_gbp": harga,
                    "availability": stock
                })
            except Exception as e:
                print(f"Terjadi kesalahan saat memproses buku: {e}")
        print(f"Halaman {page} selesai di-scrape.")
    driver.quit()

    #menyimpan hasil ke csv
    df = pd.DataFrame(data_buku)
    df.to_csv("data_buku_raw.csv", index=False)
    print(f"\n🎉 Selesai! Total {len(df)} data berhasil dikumpulkan ke 'data_buku_raw.csv'.\n")

if __name__ == "__main__":
    # Angka 5 berarti akan mengambil 5 halaman (100 data)
    jalankan_scraper_edge(50)