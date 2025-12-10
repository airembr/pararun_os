from typing import Protocol, Optional, Any, Callable


class QueueProtocol(Protocol):

    def publish(self, payload, on_error: Callable) -> Optional[Any]:  # Should return ID if None means error
        """
        Must serialize and publish data. Should return ID if None means error
        """

        pass

    def consumer(self):
        """
        Must read and deserialize data
        :return:
        """
        pass

    def data_bus(self):
        pass
