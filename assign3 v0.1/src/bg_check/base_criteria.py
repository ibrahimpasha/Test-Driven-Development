from abc import ABC, abstractmethod

class BaseCriteria(ABC): #Feedback: no need for this, Python is pretty dynamic and don't need this ceremony
  @abstractmethod
  def evaluate_criteria(self): #pragma: no cover
    pass