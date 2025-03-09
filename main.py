from adapter.repositories.kaggle_repo import KaggleRepository
from application.use_cases.auth_kaggle import AuthenticateKaggleUseCase
from application.use_cases.eda_report import GenerateEDAReportUseCase
from infrastructure.logging.logging_config import setup_logging

def main():
    setup_logging()
    dataset_name = "mushroom-classification"
    file_name = "mushrooms.csv"

    kaggle_repo = KaggleRepository()
    auth_use_case = AuthenticateKaggleUseCase(kaggle_repo)
    auth_use_case.authenticate()

    eda_use_case = GenerateEDAReportUseCase()
    eda_use_case.generate_report(file_name)

if __name__ == "__main__":
    main()