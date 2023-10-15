import os
from dotenv import load_dotenv

load_dotenv()
bucket_name=os.getenv("BUCKET_NAME")
dbt_file_path=os.getenv("DBT_FILE_PATH")

S3_ACCESS_KEY_ID=os.getenv("S3_ACCESS_KEY_ID")
S3_SECRET_ACCESS_KEY=os.getenv("S3_SECRET_ACCESS_KEY")
