from decorators import Consumer
from serializers import JSONMessageSerializer


@Consumer('test-event')
@JSONMessageSerializer
def test_event_consumer(message):
    print(f'Received: {message.data}')


@Consumer('test-event-3')
@JSONMessageSerializer
def test_event_consumer_2(message):
    print(f'Received: {message.data}')
