import asyncio
from time import sleep

import boto3

from globals import CONSUMERS
import consumers


async def start_consumer_loop(consumer):
    sqs = boto3.resource('sqs')
    queue = sqs.create_queue(QueueName=consumer.event_name)
    # queue = sqs.get_queue_by_name(QueueName=consumer.event_name)
    while True:
        print('Getting messages...')
        for message in queue.receive_messages(WaitTimeSeconds=20):
            print(f'Passing message to handler')
            consumer.event_handler(message)
            message.delete()
        print('Sleeping...')
        sleep(1)


async def start_async():
    await asyncio.wait(
        [start_consumer_loop(consumer) for consumer in CONSUMERS])


def start_loop():
    print(f'Receiving messages.')
    asyncio.run(start_async())
    print('Finished!')
