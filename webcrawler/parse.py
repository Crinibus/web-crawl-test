from warcio.archiveiterator import ArchiveIterator
import json


def parse_datachunk(stream) -> list[tuple[str, list[str]]]:
    records_with_image_urls: list[tuple[str, list[str]]] = []

    for record in ArchiveIterator(stream):
        if record.rec_type == "warcinfo":
            continue

        target_url = record.rec_headers.get_header("WARC-Target-URI")

        contents_raw = record.content_stream().read().decode("utf-8")
        contents = json.loads(contents_raw)

        links = (
            contents.get("Envelope")
            .get("Payload-Metadata")
            .get("HTTP-Response-Metadata", {})
            .get("HTML-Metadata", {})
            .get("Links")
        )

        if links is None:
            continue

        img_links = [link.get("url") for link in links if "IMG" in link.get("path", "THIS IS FOR NO ERROR")]

        if not img_links:
            continue

        records_with_image_urls.append((target_url, img_links))

    return records_with_image_urls
