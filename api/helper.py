from requests import Response

CITATION_KEY = 'citation'

def parse(key: str, response: Response):
    return response.json()[key]