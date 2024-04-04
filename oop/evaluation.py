class Evaluation:

    def __init__(self, client_name, score):
        self._client_name = client_name
        self._score = score

    def __str__(self):
        return f"Cliente: {self.client_name} avaliou com nota {self.score}"

    @property
    def client_name(self):
        return self._client_name
    
    @property
    def score(self):
        return self._score