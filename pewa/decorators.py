from globals import CONSUMERS


class Consumer:
    def __init__(
            self,
            event=None,
            attributes=None,
            sqs_attr=None,
            sns_attr=None,
    ):
        if not event:
            raise Exception('Must inform Consumer event name.')
        self.event_name = event
        self.receive_message_attributes = attributes
        self.sqs_attr = sqs_attr
        self.sns_attr = sns_attr

    def __call__(self, handler):
        self.consumer_name = handler.__name__
        self.event_handler = handler
        handler.config = self
        CONSUMERS.append(self)
        print(f'Registered consumer: {self.consumer_name} for '
              f'event {self.event_name}')
        return handler


class GroupConsumer:
    def __init__():
        pass
