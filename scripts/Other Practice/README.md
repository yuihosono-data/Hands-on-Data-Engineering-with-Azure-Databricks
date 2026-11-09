## Process Description
1. Specify the catalog name
2. Manually define schema names and table names
3. Load a CSV file containing schema names and table names
4. Convert the loaded DataFrame into a Python list
5. Retrieve all existing schemas in the catalog
6. Retrieve all existing tables in the catalog
7. Convert the retrieved table list into a Python set
8. Check whether each target table exists in the set
9. Convert results into a Spark DataFrame
