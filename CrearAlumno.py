import boto3
import json

def lambda_handler(event, context):
    # Parsear body
    body = event['body']
    if isinstance(body, str):
        body = json.loads(body)

    # Entrada
    tenant_id = body['tenant_id']
    alumno_id = body['alumno_id']
    alumno_datos = body['alumno_datos']

    # Proceso
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('t_alumnos')
    alumno = {
        'tenant_id': tenant_id,
        'alumno_id': alumno_id,
        'alumno_datos': alumno_datos
    }
    response = table.put_item(Item=alumno)

    # Salida
    return {
        'statusCode': 200,
        'mensaje': 'Alumno creado correctamente'
    }
