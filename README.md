# Automated Web Scraping Pipeline & Data Quality Audit Suite

Welcome to the **Automated Data QA Pipeline** project repository!

This project is designed to simulate an end-to-end Data Quality Assurance (QA) workflow. The automated pipeline crawls web user interfaces, extracts large-scale data, ingests it into a PostgreSQL relational database, executes data integrity validation via SQL queries, and visualizes the audit metrics in an executive Microsoft Excel dashboard.

---

## Table of Contents

- [ Project Background](#-project-background)
- [ Tech Stack & Tools](#️-tech-stack--tools)
- [ Pipeline Architecture](#️-pipeline-architecture)
- [ SQL Audit Results & QA Findings (Edge Case)](#-sql-audit-results--qa-findings-edge-case)
- [ Step-by-Step Local Setup Guide](#-step-by-step-local-setup-guide)
- [ Repository Structure](#-repository-structure)

---

##  Project Background

In real-world data engineering and SQA environments, raw web-scraped or ingested datasets often contain anomalies—such as missing values (`NULL`), zero prices, corrupted text formats, or duplicate entries.

Key objectives of this project:

1. **UI Automation Scraper:** Automatically extract 1,000 product records across 50 web pages from `books.toscrape.com` using Microsoft Edge.
2. **Database Ingestion (ETL):** Perform initial data cleaning and automate batch ingestion into a PostgreSQL database.
3. **Data Quality Assurance (SQL Testing):** Execute targeted SQL audit queries to validate data integrity constraints.
4. **Executive Reporting:** Build a visual Data Quality Dashboard showing pass/fail metrics in Microsoft Excel.

---

##  Tech Stack & Tools

-  **Python 3.12+** – Core programming language for pipeline automation.
-  **Selenium WebDriver (Microsoft Edge)** – Browser UI navigation & web scraping.
-  **PostgreSQL 16 & pgAdmin 4** – Relational Database Management System (RDBMS).
-  **Psycopg2** – Python-to-PostgreSQL transactional database driver.
-  **Pandas** – Data manipulation, transformation, and CSV export.
-  **Microsoft Excel** – Visual audit reporting (`COUNTIF`/`IF` formulas, Conditional Formatting, and Pivot Charts).
-  **Git & GitHub** – Version control and portfolio documentation.

---

##  Pipeline Architecture

```text
Web Source (50 Pages - 1,000 Items)
       │
       ▼ (Selenium Edge - Headless Mode)
Raw Data Extractions (data_buku_raw.csv)
       │
       ▼ (Python psycopg2 - Transactional Batch Insert)
PostgreSQL Database (data.sql)
       │
       ▼ (Export & Format Visualization)
Excel Executive Dashboard (Data_Quality_1000.xlsx)
```
