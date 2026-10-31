-- 1. Cek Anomali Harga (NULL, 0, atau Minus)
SELECT id, title, price_gbp 
FROM products 
WHERE price_gbp IS NULL OR price_gbp <= 0;

-- 2. Cek Duplikat Murni (Judul DAN Harga Sama Persis)
SELECT title, price_gbp, COUNT(*) as jumlah_duplikat
FROM products
GROUP BY title, price_gbp
HAVING COUNT(*) > 1;

-- 3. Cek Varian Produk (Judul Sama, Harga Beda)
SELECT title, COUNT(DISTINCT price_gbp) as variasi_harga, COUNT(*) as total_item
FROM products
GROUP BY title
HAVING COUNT(*) > 1 AND COUNT(DISTINCT price_gbp) > 1;

-- 4. Ringkasan Statistik Kualitas Data (Summary])
SELECT 
    COUNT(*) AS total_rekord,
    COUNT(price_gbp) AS data_harga_valid,
    ROUND(AVG(price_gbp), 2) AS rata_rata_harga,
    MAX(price_gbp) AS harga_tertinggi,
    MIN(price_gbp) AS harga_terendah
FROM products;