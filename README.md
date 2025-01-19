# AWS Glue + Apache Iceberg ETL Project

This guide walks you through the steps to build a batch data pipeline using AWS Glue, Apache Iceberg, PySpark, and AWS S3.

## Overview
This project demonstrates batch processing with AWS Glue, Apache Iceberg, and Athena using PySpark for ETL. Data is processed and stored as Iceberg tables in S3, with Athena for querying.

---

## Features
- AWS Glue for metadata management and ETL jobs.
- Apache Iceberg for efficient table formats with time travel and schema evolution.
- Athena for querying processed data.
- PyIceberg for programmatic interaction with Iceberg tables.

---

---

## Dataset
The dataset used in this project is the NYC Taxi Trip Data. You can download it from the following link:  
**[NYC Taxi Trip Data on Kaggle](https://www.kaggle.com/datasets/elemento/nyc-yellow-taxi-trip-data?resource=download)**

---

## Architecture
![alt text](<Apache Iceberg Architecture.jpg>)

## Steps to Set Up

1. **Create S3 Buckets**:
   - `nyc-taxi-data-project-raw` for raw data.
   - `nyc-taxi-data-project-warehouse` for processed data.
   - `nyc-taxi-data-project-results` for Athena query results.

2. **Upload Raw Data**:
   Upload `sample_nyc_taxi_data.csv` to `nyc-taxi-data-project-raw`.

3. **Create Glue Database**:
   - Name: `nyc_taxi_data_db`.

4. **Create Glue Crawler**:
   - Input S3 path: `s3://nyc-taxi-data-project-raw/`.
   - Output Database: `nyc_taxi_data_db`.

5. **Submit Glue ETL Job**:
   - Use `scripts/glue_etl_job.py`.

6. **Run Athena Queries**:
   - Use `scripts/test_queries.sql`.

---

## Medium Article
Learn more about setting up this project step-by-step in my Medium article:  
**[Getting Started with AWS Glue and Apache Iceberg for ETL Pipelines](https://medium.com/@gaganabbot04/getting-started-with-aws-glue-and-apache-iceberg-for-etl-pipelines-9c04b233b8b9)**

---
