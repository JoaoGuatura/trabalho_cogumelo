class AuthenticateKaggleUseCase:
    def __init__(self, repository):
        self.repository = repository

    def authenticate(self):
        print("🔑 Autenticando no Kaggle...")
        self.repository.authenticate()
        print("✅ Autenticado com sucesso!")