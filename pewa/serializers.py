import json


def JSONMessageSerializer(event_handler):
    def wrapper(message):
        message.data = json.loads(message.body)
        return event_handler(message)

    return wrapper
