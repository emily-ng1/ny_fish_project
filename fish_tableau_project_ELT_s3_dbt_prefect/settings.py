import os
from dotenv import load_dotenv

load_dotenv()
DB_NAME=os.getenv("DB_NAME")
DB_USER=os.getenv("DB_USER")
DB_PASSWORD=os.getenv("DB_PASSWORD")

TEST_DB_NAME=os.getenv("TEST_DB_NAME")
TEST_DB_USER=os.getenv("TEST_DB_USER")
TEST_DB_PASSWORD=os.getenv("TEST_DB_PASSWORD")

bucket_name=os.getenv("BUCKET_NAME")
dbt_file_path=os.getenv("DBT_FILE_PATH")

S3_ACCESS_KEY_ID=os.getenv("S3_ACCESS_KEY_ID")
S3_SECRET_ACCESS_KEY=os.getenv("S3_SECRET_ACCESS_KEY")
