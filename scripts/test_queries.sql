-- Query processed Iceberg table
SELECT * 
FROM nyc_taxi_data_db.processed_data_table 
LIMIT 10;

-- Filter data
SELECT vendorid, passenger_count, trip_distance 
FROM nyc_taxi_data_db.processed_data_table 
WHERE trip_distance > 10;
