from typing import List

import easyocr
from PIL import Image


class OCRService:
    def __init__(self, languages: List[str] = ["en", "pt"]):
        self.reader = easyocr.Reader(languages)

    def read_text(self, image_path):
        image = Image.open(image_path)
        result = self.reader.readtext(image, detail=0)
        return " ".join(str(item) for item in result)
