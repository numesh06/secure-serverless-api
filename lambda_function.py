import json


def lambda_handler(event, context):
    # Log the incoming event for debugging
    print("Received event:", json.dumps(event))

    # Extract data from the event
    body = event.get('body')
    if body:
        try:
            data = json.loads(body)
            message = data.get('message', 'Hello from a secure Lambda function!')
        except json.JSONDecodeError:
            return {
                'statusCode': 400,
                'body': json.dumps({'error': 'Invalid JSON'})
            }
    else:
        message = 'Hello from a secure Lambda function!'

    # Return the response
    return {
        'statusCode': 200,
        'body': json.dumps({'message': message})
    }
