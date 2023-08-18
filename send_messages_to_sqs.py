import json
import boto3
import configparser


def send_messages_sqs(session, queue_url, messages):
    sqs = session.client('sqs')

    for message in messages:
        response = sqs.send_message(
            QueueUrl=queue_url,
            MessageBody=json.dumps(message)
        )
        print(f"Sent message: {response['MessageId']}")


def main():
    config = configparser.ConfigParser()
    config.read('config.ini')

    access_key = config['aws']['aws_access_key_id']
    secret_key = config['aws']['aws_secret_access_key']
    session_token = config['aws']['aws_session_token']
    region = config['aws']['region']

    session = boto3.Session(
        aws_access_key_id=access_key,
        aws_secret_access_key=secret_key,
        aws_session_token=session_token,
        region_name=region
    )

    queue_url = config['aws']['queue_url']

    with open('messages.json', 'r') as file:
        messages = json.load(file)

    send_messages_sqs(session, queue_url, messages)


if __name__ == '__main__':
    main()
