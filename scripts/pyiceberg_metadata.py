from pyiceberg.catalog import load_catalog

# Load Glue Catalog
catalog = load_catalog("glue", uri="aws", warehouse="s3://nyc-taxi-data-project-warehouse/")

# Load the Iceberg table
table = catalog.load_table("nyc_taxi_data_db.processed_data_table")

# Print schema
print("Table Schema:", table.schema())

# List snapshots
print("Snapshots:", table.snapshots())
