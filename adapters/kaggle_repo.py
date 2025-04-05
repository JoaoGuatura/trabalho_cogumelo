from domain.interfaces.repository_interface import RepositoryInterface
import kaggle

class KaggleRepository(RepositoryInterface):
    def authenticate(self):
        kaggle.api.authenticate()

    def download_dataset(self, dataset_name: str, path: str = "data"):
        kaggle.api.dataset_download_files(dataset_name, path=path, unzip=True)
