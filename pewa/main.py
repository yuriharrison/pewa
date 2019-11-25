import json
import time
import logging
from datetime import datetime

import boto3
import click
from decouple import config

from loop import start_loop


@click.group()
def program():
    pass


@program.command()
def start():
    start_loop()


@program.command()
@click.argument('event')
@click.option('-n', '--number', 'num', default=1)
@click.option('-d', '--delay', 'delay', default=1, type=float)
def publish(event, num, delay):
    sqs = boto3.resource('sqs')
    queue = sqs.create_queue(QueueName=event)
    print(f'Sending {num} message(s) each {delay} second(s).')
    for _ in range(num):
        time.sleep(delay)
        queue.send_message(
            MessageBody=json.dumps(dict(time=str(datetime.now()))))
        print('Message sent!')
    print('Finish sending!')


@program.command()
@click.option('-w', '--wait-time', 'wait_time', default=0)
@click.option('-s', '--sleep-time', 'sleep', default=0.1)
def receive(wait_time, sleep):
    print(f'Receiving messages. Wait Time: {wait_time}')
    try:
        while True:
            print('Getting messages...')
            for message in queue.receive_messages(WaitTimeSeconds=wait_time):
                print(f'Received: {message.body}')
                message.delete()
            print('Sleeping...')
            time.sleep(sleep)
    except KeyboardInterrupt:
        print('Stopping...')
    print('Finished!')


if '__main__' == __name__:
    program()