import sys
from pyspark.context import SparkContext
from pyspark.sql import SparkSession

if __name__ == "__main__":
    sc = SparkContext()
    spark = SparkSession.builder \
        .appName("Iceberg ETL Job") \
        .config("spark.sql.catalog.glue_catalog", "org.apache.iceberg.spark.SparkCatalog") \
        .config("spark.sql.catalog.glue_catalog.warehouse", "s3://nyc-taxi-data-project-warehouse/") \
        .config("spark.sql.catalog.glue_catalog.catalog-impl", "org.apache.iceberg.aws.glue.GlueCatalog") \
        .getOrCreate()

    # Read raw data
    raw_data = spark.read.csv("s3://nyc-taxi-data-project-raw/sample_nyc_taxi_data.csv", header=True, inferSchema=True)

    # Write to Iceberg
    raw_data.writeTo("glue_catalog.nyc_taxi_data_db.processed_data_table").createOrReplace()
