import boto3
import json
from boto3.dynamodb.conditions import Key

def lambda_handler(event, context):
    # Parsear body
    body = event['body']
    if isinstance(body, str):
        body = json.loads(body)
    
    # Entrada
    tenant_id = body['tenant_id']
    
    # Proceso
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('t_alumnos')
    response = table.query(
        KeyConditionExpression=Key('tenant_id').eq(tenant_id)
    )
    items = response['Items']
    num_reg = response['Count']
    
    # Salida
    return {
        'statusCode': 200,
        'tenant_id': tenant_id,
        'num_reg': num_reg,
        'alumnos': items
    }
