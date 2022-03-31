from abc import ABC, abstractmethod
class Battery(ABC):

    @abstractmethod
    def needs_service():
        pass


class NubbinBattery(Battery):
    def __init__(self, last_service_date, current_date):
        self._last_service_date = last_service_date
        self._current_date = current_date


    def needs_service(self):
        service_threshold_date = self._last_service_date.replace(year=self._last_service_date.year + 4)
        return service_threshold_date < self._current_date

class SplinderBattery(Battery):
    def __init__(self, last_service_date, current_date):
        self._last_service_date = last_service_date
        self._current_date = current_date


    def needs_service(self):
        service_threshold_date = self._last_service_date.replace(year=self._last_service_date.year + 2)
        return service_threshold_date < self._current_date