import subprocess

db_schema = 'SCHEMA=geodata'
overwrite_option = "OVERWRITE=YES"
geom_type = "MULTILINESTRING"
output_format = "PostgreSQL"

db_connection = """PG:host=localhost port=5432 user=alim dbname=spatial password=120507"""

input_shp = "../geodata/bikeways.shp"

subprocess.call(["ogr2ogr","-lco", db_schema, "-lco", overwrite_option, "-nlt", geom_type, "-f", output_format, db_connection, input_shp])
