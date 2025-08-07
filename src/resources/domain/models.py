from resources.domain.value_objects import ResourceUrl

class Resource:
  def __init__(self, resource_url: ResourceUrl) -> None:
    self._resource_url = resource_url

  @classmethod
  def create(cls, resource_url: ResourceUrl) -> "Resource":
    return cls(resource_url)
  
  def url(self) -> ResourceUrl:
    return self._resource_url