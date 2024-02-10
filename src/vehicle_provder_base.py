from src.vehicle_entity import VehicleEntity
from abc import ABC, abstractmethod

class VehicleProviderBase(ABC):

    data_source: str

    @abstractmethod
    def _fetch_plate_page(self, plate: str) -> str:
        pass

    @abstractmethod
    def _parse_plate_page(self, plate_page: str) -> VehicleEntity:
        pass

    @abstractmethod
    def fetch_vehicle(self, plate: str) -> VehicleEntity:
        pass

