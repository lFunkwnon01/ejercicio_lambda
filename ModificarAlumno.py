import boto3


def lambda_handler(event, context):
    # Entrada - datos vienen del BODY (es PUT)
    tenant_id = event['body']['tenant_id']
    alumno_id = event['body']['alumno_id']
    alumno_datos = event['body']['alumno_datos']

    # Proceso
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('t_alumnos')

    # Verificar que el alumno existe antes de modificar
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

    # Salida (json)
    return {
        'statusCode': 200,
        'mensaje': f'Alumno {alumno_id} modificado correctamente',
        'updated': response.get('Attributes', {})
    }