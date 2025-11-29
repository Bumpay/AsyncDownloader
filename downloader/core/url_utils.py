from urllib.parse import urlparse


def is_valid_url(url: str) -> bool:
    if not url.strip():
        return False

    parsed_url = urlparse(url)

    if parsed_url.scheme not in ['http', 'https']:
        return False

    if not parsed_url.netloc:
        return False

    return True
