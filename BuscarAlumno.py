import boto3


def lambda_handler(event, context):
    # Entrada - parámetros vienen del PATH de la URL
    tenant_id = event['path']['tenant_id']
    alumno_id = event['path']['alumno_id']

    # Proceso
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('t_alumnos')

    response = table.get_item(
        Key={
            'tenant_id': tenant_id,
            'alumno_id': alumno_id
        }
    )

    alumno = response.get('Item', None)

    # Salida (json)
    if alumno:
        return {
            'statusCode': 200,
            'alumno': alumno
        }
    else:
        return {
            'statusCode': 404,
            'mensaje': f'Alumno {alumno_id} no encontrado en tenant {tenant_id}'
        }