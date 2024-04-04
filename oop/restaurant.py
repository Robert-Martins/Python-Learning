from evaluation import Evaluation

class Restaurant:

    restaurants = []

    def __init__(self, name, category):
        self._name = name.title()
        self._category = category.upper()
        self._active = False
        self._evaluations = []
        Restaurant.restaurants.append(self)

    def __str__(self):
        return f"{self.name} - {self.category} -> {self.active} | Avaliação Média: {self.average_evaluations_score()}"
    
    def update_status(self):
        self._active = not self._active

    def add_evaluation(self, evaluation):
        self._evaluations.append(evaluation)

    @classmethod
    def get_restaurants(cls):
        return cls.restaurants
    
    @classmethod
    def hasnt_restaurants(cls):
        return len(cls.restaurants) == 0
    
    @property
    def name(self):
        return self._name
    
    @property
    def category(self):
        return self._category

    @property
    def active(self):
        return "Ativo" if self._active else "Inativo"
    
    @property
    def evaluations(self):
        return self._evaluations
    
    def total_evaluations_score(self):
        return 0 if not self.evaluations else sum(evaluation.score for evaluation in self.evaluations)
    
    def total_evaluations(self):
        return len(self.evaluations)
    
    def average_evaluations_score(self):
        total_evaluations_score = self.total_evaluations_score()
        total_evaluations = self.total_evaluations()
        return 0 if total_evaluations_score == 0 or total_evaluations == 0 else total_evaluations_score / total_evaluations