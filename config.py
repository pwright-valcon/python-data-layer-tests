import os

example_rds_db_config = {
    'dbname': os.environ.get('EXAMPLE_RDS_DB_NAME', ''),
    'user': os.environ.get('EXAMPLE_RDS_USER', ''),
    'password': os.environ.get('EXAMPLE_RDS_PASSWORD', ''),
    'host': os.environ.get('EXAMPLE_RDS_HOST', ''),
    'port': os.environ.get('EXAMPLE_RDS_PORT', '')
}
