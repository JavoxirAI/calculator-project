import csv
import os.path


def read(filename: str) -> list[dict]:
    path = f"data/{filename}"
    if os.path.exists(path):
        with open(file=path, mode="r", encoding="UTF-8", newline='') as file:
            reader = csv.DictReader(file)
            return list(reader)
    return []