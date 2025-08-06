from .repositories import Resource, ResourceRepository

class PostgreSQLResourcesRepository(ResourceRepository):
  def get(self) -> Resource:
    return None