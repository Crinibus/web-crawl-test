from io import BufferedReader
import csv


def get_file_stream(file_path: str, mode: str) -> BufferedReader:
    return open(file_path, mode)


def append_row_to_csv(file_path: str, data_row: list[str]) -> None:
    with open(file_path, "a", encoding="utf8", newline="") as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(data_row)


def append_rows_to_csv(file_path: str, data_rows: list[list[str]]) -> None:
    with open(file_path, "a", encoding="utf8", newline="") as file:
        csv_writer = csv.writer(file)

        for data_row in data_rows:
            csv_writer.writerow(data_row)
