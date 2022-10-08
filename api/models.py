import api.helper as helper

class Citation:

    def __init__(self, response):
        """
        {
          "id": 0,
          "reference_id": 0,
          "pages": "string",
          "created_at": "2022-10-08T03:19:52.898Z",
          "updated_at": "2022-10-08T03:19:52.898Z"
        }
        """

        self.meta = helper.parse(helper.CITATION_KEY, response)
        self.id = self.meta['id']
        self.reference_id = self.meta['reference_id']
        self.pages = self.meta['pages']
        self.created_at = self.meta['created_at']
        self.updated_at = self.meta['updated_at']

    def __str__(self):
        return f'{self.id} {self.pages}'

class HistoryItem:

    def __int__(self, json):
        pass