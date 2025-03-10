from abc import ABC, abstractmethod


class BaseEnergyClient(ABC):
    """Classe base para todas as concessionárias de energia."""

    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password

    @abstractmethod
    def login(self):
        """Realiza o login no portal da concessionária."""
        pass

    @abstractmethod
    def download_invoice(self, account_number: str):
        """Baixa a fatura de energia de um cliente."""
        pass
