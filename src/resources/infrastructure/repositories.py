from sqlmodel import Field, SQLModel, Session, create_engine
from resources.domain.models import Resource
from resources.domain.repositories import ResourcesRepository

class ResourceModel(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    url: str

engine = create_engine("sqlite:///database.db")

SQLModel.metadata.create_all(engine)

class SQLModelResourceRepository(ResourcesRepository):
  def all(self) -> list[Resource]:
    pass

  def save(self, resource: Resource) -> None:
    resource_model = ResourceModel(url=resource.url().value)
    with Session(engine) as session:
       session.add(resource_model)
       session.commit()