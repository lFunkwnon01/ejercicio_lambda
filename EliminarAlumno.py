import boto3


def lambda_handler(event, context):
    # Entrada - parámetros vienen del PATH de la URL
    tenant_id = event['path']['tenant_id']
    alumno_id = event['path']['alumno_id']

    # Proceso
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('t_alumnos')

    # Verificar que el alumno existe antes de eliminar
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

    response = table.delete_item(
        Key={
            'tenant_id': tenant_id,
            'alumno_id': alumno_id
        }
    )

    # Salida (json)
    return {
        'statusCode': 200,
        'mensaje': f'Alumno {alumno_id} eliminado correctamente',
        'response': response
    }