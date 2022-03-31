from abc import ABC, abstractmethod
class Engine(ABC):

    @abstractmethod
    def needs_service():
        pass


class CapuletEngine(Engine):
    def __init__(self, last_service_mileage,current_mileage):
        self._current_mileage = current_mileage
        self._last_service_mileage = last_service_mileage

    def needs_service(self):
        return self._current_mileage - self._last_service_mileage > 30000

class WilloughbyEngine(Engine):
    def __init__(self, last_service_mileage,current_mileage):
        self._current_mileage = current_mileage
        self._last_service_mileage = last_service_mileage

    def needs_service(self):
        return self._current_mileage - self._last_service_mileage > 60000

class SternmanEngine(Engine):
    def __init__(self, warning_light_is_on):
        self._warning_light_is_on = warning_light_is_on

    def engine_should_be_serviced(self):
        return self._warning_light_is_on                