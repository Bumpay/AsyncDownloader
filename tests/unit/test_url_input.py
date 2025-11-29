from downloader.core.url_utils import is_valid_url


def test_empty_string():
    assert is_valid_url('') == False


def test_whitespace():
    assert is_valid_url(' ') == False


def test_valid_url():
    assert is_valid_url('https://www.google.com') == True


def test_invalid_scheme():
    assert is_valid_url('ftp://www.google.com') == False


def test_missing_scheme():
    assert is_valid_url('www.google.com') == False


def test_localhost():
    assert is_valid_url('http://localhost') == True