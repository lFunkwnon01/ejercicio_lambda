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
    
    # Verificar que existe
    check = table.get_item(
        Key={
            'tenant_id': tenant_id,
            'alumno_id': alumno_id
        }
    )
    if 'Item' not in check:
        return {
            'statusCode': 404,
            'mensaje': f'Alumno {alumno_id} no encontrado en tenant {tenant_id}'
        }
    
    response = table.update_item(
        Key={
            'tenant_id': tenant_id,
            'alumno_id': alumno_id
        },
        UpdateExpression='SET alumno_datos = :datos',
        ExpressionAttributeValues={
            ':datos': alumno_datos
        },
        ReturnValues='UPDATED_NEW'
    )
    
    # Salida
    return {
        'statusCode': 200,
        'mensaje': f'Alumno {alumno_id} modificado correctamente',
        'updated': response.get('Attributes', {})
    }
