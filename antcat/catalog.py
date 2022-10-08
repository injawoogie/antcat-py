from api.models import Citation
from api import raw_response as urls


def get_citation(self, citation_id: int) -> Citation:
    """
    Gets a single citation from AntCat Api using a single citation id.
    Returns None if the citation record is not found.

    :param citation_id:
    :return: Citation or None
    """

    response, found = urls.get_citation_from(citation_id)
    return Citation(response) if found else None


def get_history_item(self, history_item_id):
    pass


citation = get_citation(154418)
print(citation)