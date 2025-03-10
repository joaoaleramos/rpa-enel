import requests

from rpa_enel.clients.base_client import BaseEnergyClient


class EnelClient(BaseEnergyClient):
    BASE_URL = "https://www.enel.com.br/portal/"

    def login(self):
        """Faz login no portal da Enel."""
        payload = {"username": self.username, "password": self.password}
        response = requests.post(f"{self.BASE_URL}/login", json=payload)

        if response.status_code == 200:
            self.session_token = response.json().get("token")
            return True
        return False

    def download_invoice(self, account_number: str):
        """Baixa a fatura de energia da Enel."""
        headers = {"Authorization": f"Bearer {self.session_token}"}
        response = requests.get(
            f"{self.BASE_URL}/invoice/{account_number}", headers=headers
        )

        if response.status_code == 200:
            with open(f"data/faturas/enel_{account_number}.pdf", "wb") as file:
                file.write(response.content)
            return f"Fatura Enel {account_number} baixada com sucesso."
        return "Erro ao baixar fatura."
