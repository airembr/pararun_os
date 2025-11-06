from pararun.model.adapter import Adapter
from pararun.model.data_bus import DataBus, DataBusSubscription
from pararun.service.singleton import Singleton

from pararun.protocol.queue_client_protocol import QueueProtocol


class DummyAdapter(QueueProtocol):

    def __init__(self, data_bus: DataBus):
        pass

class DeferAdapterSelector(metaclass=Singleton):
    def get(self, adapter_name, queue_tenant: str) -> Adapter:
        return Adapter(
            serializers={},
            adapter_protocol=DummyAdapter(
                DataBus(
                    topic='',
                    factory=None,
                    subscription=DataBusSubscription(
                        subscription_name="collector",
                        consumer_name="collector",
                        consumer_type=None,
                        initial_position='earliest',
                        receiver_queue_size=1000
                    )
                ))
        )
