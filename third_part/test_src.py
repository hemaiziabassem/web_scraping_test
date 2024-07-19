import json

from src import parse_categories


def test_parse_categories():
    categories = parse_categories()
    with open('./expected_categories.json') as f:
        expected_categories = json.load(f)
    assert categories == expected_categories
