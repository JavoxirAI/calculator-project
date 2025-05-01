import csv
import os.path


def read(filename: str) -> list[dict]:
    path = f"data/{filename}"
    if os.path.exists(path):
        with open(file=path, mode="r", encoding="UTF-8", newline='') as file:
            reader = csv.DictReader(file)
            return list(reader)
    return []


def write(filename: str, data: list[dict]) -> None:
    if not data:
        return
    path = f"data/{filename}"
    with open(file=path, mode="w", encoding="UTF-8", newline='') as file:
        writer = csv.DictWriter(file, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)