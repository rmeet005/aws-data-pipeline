import boto3
import mysql.connector
from botocore.exceptions import NoCredentialsError

def read_data_from_s3(bucket_name, file_key):
    s3 = boto3.client('s3')
    try:
        response = s3.get_object(Bucket="my-buck-4", Key="data.txt")
        data = response['Body'].read().decode('utf-8')
        print("Data retrieved from S3.")
        print(data)
        return data
    except NoCredentialsError:
        print("Credentials not available.")
        return None

def push_data_to_rds(data, rds_endpoint, username, password, database):
    try:
        connection = mysql.connector.connect(
            host="mydb1.cvsyuyy0kztf.ap-south-1.rds.amazonaws.com",
            user="admin",
            password="admin12345",
            database="my_raval"
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

def main():
    bucket_name = "my-buck-4"
    file_key = "data.txt"
    rds_endpoint = "mydb1.cvsyuyy0kztf.ap-south-1.rds.amazonaws.com"
    username = "admin"
    password = "admin12345"
    database = "my_raval"
    data = read_data_from_s3(bucket_name, file_key)
    if data:
        if not push_data_to_rds(data, rds_endpoint, username, password, database):
           """ push_data_to_glue(data, glue_database, glue_table)"""

if __name__ == "__main__":
    main()

