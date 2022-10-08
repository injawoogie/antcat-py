import requests
from requests import Response


ROOT_URL = 'https://antcat.org/'
VERSION = 'v1/'
AUTHOR_NAMES = 'author_names/'
AUTHORS = 'authors/'
CITATIONS = 'citations/'
HISTORY_ITEMS = 'history_items/'
JOURNALS = 'journals/'
NAMES = 'names/'
PROTONYMS = 'protonyms/'
PUBLISHERS = 'publishers/'
REFERENCE_AUTHOR_NAMES = 'reference_author_names/'
REFERENCE_DOCUMENTS = 'reference_documents/'
REFERENCE_SECTIONS = 'reference_sections/'
REFERENCES = 'references/'
TAXA = 'taxa/'
TAXA_SEARCH = 'taxa/search/'
STARTS_AT = '?starts_at='


def requestor(func):
    def maker(*args, **kwargs) -> (Response, bool):
        response = requests.get(url=f"{ROOT_URL}{VERSION}{func(*args, **kwargs)}")
        found = True if response.status_code == 200 else False
        return response, found
    return maker


@requestor
def get_author_name_from(author_name_id: int) -> str:
    """

    :rtype: object
    """
    return f"{AUTHOR_NAMES}{author_name_id}"


@requestor
def get_author_from(author_id: int) -> str:
    return f"{AUTHORS}{author_id}"


@requestor
def get_citation_from(citation_id: int) -> str:
    return f"{CITATIONS}{citation_id}"


@requestor
def get_history_item_from(history_item_id: int) -> str:
    return f"{HISTORY_ITEMS}{history_item_id}"


@requestor
def get_journal_from(journal_id: int) -> str:
    return f"{JOURNALS}{journal_id}"


@requestor
def get_name_from(name_id: int) -> str:
    return f"{NAMES}{name_id}"


@requestor
def get_protonym_from(protonym_id: int) -> str:
    return f"{PROTONYMS}{protonym_id}"


@requestor
def get_publisher_from(publisher_id: int) -> str:
    return f"{PUBLISHERS}{publisher_id}"


@requestor
def get_reference_author_name_from(reference_author_name_id: int) -> str:
    return f"{REFERENCE_AUTHOR_NAMES}{reference_author_name_id}"


@requestor
def get_reference_document_from(reference_document_id: int) -> str:
    return f"{REFERENCE_DOCUMENTS}{reference_document_id}"


@requestor
def get_reference_section_from(reference_section_id: int) -> str:
    return f"{REFERENCE_SECTIONS}{reference_section_id}"


@requestor
def get_reference_from(reference_id: int) -> str:
    return f"{REFERENCES}{reference_id}"


@requestor
def get_taxa_from(taxa_id: int) -> str:
    return f"{TAXA}{taxa_id}"


@requestor
def get_taxa_search_from(taxa: str) -> str:
    return f"{TAXA_SEARCH}{taxa}"
