from abc import ABC, abstractmethod
from .repositories import Resource 

class ResourceRepository(ABC):
  @abstractmethod
  def get(self) -> Resource: ...
    