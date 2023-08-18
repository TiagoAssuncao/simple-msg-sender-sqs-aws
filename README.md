# AWS SQS Message Sender

A Python script to send messages to AWS SQS queues. This script reads messages from an external JSON file and retrieves AWS credentials from a config file.

## Table of Contents

- [Introduction](#introduction)
- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
- [Configuration](#configuration)
- [Usage](#usage)

## Introduction

This script provides a simple way to send messages to an AWS SQS queue using the `boto3` library, which is the AWS SDK for Python. It reads messages from an external JSON file and retrieves AWS credentials from a config file. The script is designed to be easy to use and customizable for your specific use case.

## Prerequisites

Before you begin, make sure you have the following:

- Python (3.6 or higher) installed on your machine.
- An AWS account with access to SQS.

## Getting Started

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/your-username/aws-sqs-message-sender.git
    ```
   
2. Install the required Python packages:

    ```bash
    pip3 install boto3
    ```
   
## Configuration

Update a JSON file (messages.json) containing the messages you want to send:

```json
[
  {
    "message": "Hello World!"
  },
  {
    "message": "Hello World Again!"
  }
]
```

Update a configuration file (config.ini) containing your AWS credentials:

```ini
[aws]
aws_access_key_id = YOUR_ACCESS_KEY_ID
aws_secret_access_key = YOUR_SECRET_ACCESS_KEY
aws_session_token = YOUR_ACCESS_TOKEN_KEY
region = YOUR_AWS_REGION
queue_url = YOUR_AWS_SQS_QUEUE_URL
```

## Usage

1. Run the script:
    
    ```bash
    python send_messages_to_sqs.py
    ```

The script will read messages from the messages.json file and send them to the specified SQS queue.