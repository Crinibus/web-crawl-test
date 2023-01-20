import requests

from webcrawler.arguments import argparse_setup
from webcrawler.parse import parse_datachunk
from webcrawler.filemanager import append_rows_to_csv


def main() -> None:
    args = argparse_setup()

    for datachunk_path in args.paths:
        crawl_url = "https://data.commoncrawl.org/" + datachunk_path

        response = requests.get(crawl_url, stream=True)
        records_with_img_links = parse_datachunk(response.raw)
        append_rows_to_csv("records-img-links.csv", records_with_img_links)


if __name__ == "__main__":
    main()
