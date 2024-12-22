import boto3
import pymysql
from botocore.exceptions import NoCredentialsError

def read_data_from_s3(bucket_name, file_key):
    s3 = boto3.client('s3')
    try:
        response = s3.get_object(Bucket=my-raval-1, Key=meetpic.jpeg)
        data = response['Body'].read().decode('utf-8')
        print("Data retrieved from S3.")
        return data
    except NoCredentialsError:
        print("Credentials not available.")
        return None

def push_data_to_rds(data, rds_endpoint, username, password, database):
    try:
        connection = pymysql.connect(
            host=database-1.cvsyuyy0kztf.ap-south-1.rds.amazonaws.com,
            user=admin,
            password=root12345,
            database=database-1
        )
        cursor = connection.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS data_store (id INT AUTO_INCREMENT PRIMARY KEY, data TEXT)")
        cursor.execute("INSERT INTO data_store (data) VALUES (%s)", (data,))
        connection.commit()
        print("Data pushed to RDS.")
        connection.close()
        return True
    except Exception as e:
        print(f"RDS push failed: {e}")
        return False

"""def push_data_to_glue(data, glue_database, glue_table):
    glue_client = boto3.client('glue')
    try:
        glue_client.put_table(
            DatabaseName=glue_database,
            TableInput={
                'Name': glue_table,
                'StorageDescriptor': {
                    'Columns': [{'Name': 'data', 'Type': 'string'}],
                },
            }
        )
        print("Data pushed to Glue.")
    except Exception as e:
        print(f"Glue push failed: {e}")"""

def main():
    bucket_name = "my-raval-1"
    file_key = "meetpic.jpeg"
    rds_endpoint = "database-1.cvsyuyy0kztf.ap-south-1.rds.amazonaws.com"
    username = "admin"
    password = "root12345"
    database = "database-1"
    data = read_data_from_s3(bucket_name, file_key)
    if data:
        if not push_data_to_rds(data, rds_endpoint, username, password, database):
           """ push_data_to_glue(data, glue_database, glue_table)"""

if __name__ == "__main__":
    main()
