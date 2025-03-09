from abc import ABC, abstractmethod

class RepositoryInterface(ABC):
    @abstractmethod
    def authenticate(self):
        pass

    @abstractmethod
    def download_dataset(self, dataset_name: str, path: str):
        pass
