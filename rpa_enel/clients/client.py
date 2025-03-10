from enum import Enum

from rpa_enel.clients.enel import EnelClient


class EnergyClient(str, Enum):
    ENEL = "enel"
    NEOENERGIA = "neoenergia"


clients = {
    EnergyClient.ENEL.value: EnelClient,
}


def get_energy_client(company: str, username: str, password: str):
    """Retorna o client apropriado para a concessionária especificada."""
    company = company.lower()

    if company in clients:
        return clients[company](username, password)

    raise ValueError(f"Concessionária '{company}' não suportada.")
