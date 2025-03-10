import re

from rpa_enel.ocr.ocr_service import OCRService

ocr_service = OCRService()


def extract(self, image_path):
    """Lê a fatura e extrai o total de energia consumida (kWh)."""
    text = ocr_service.read_text(image_path)

    # Expressão regular para capturar valores numéricos seguidos de "kWh"
    pattern = r"(\d+\.?\d*)\s*kWh"

    matches = re.findall(pattern, text, re.IGNORECASE)

    if matches:
        return float(
            matches[-1]
        )  # Pegamos o último valor encontrado, pois geralmente é o total
    return None
