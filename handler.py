from pyathena import connect
import json

def lambda_handler(event, context):
    cursor = connect(s3_staging_dir='s3://aws-athena-query-results-486127124488-us-east-1/',region_name='us-east-1').cursor()
    cursor.execute("SELECT * FROM zmd.iodetail LIMIT 10")
    response = cursor.fetchall()
    print(response)
    return {
        'statusCode': 200,
        'body': json.dumps(response)
    }