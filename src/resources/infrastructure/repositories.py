from sqlmodel import Field, SQLModel, Session, create_engine, select
from resources.domain.models import Resource
from resources.domain.repositories import ResourcesRepository
from resources.domain.value_objects import ResourceUrl

class ResourceModel(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    url: str

engine = create_engine("sqlite:///database.db")

SQLModel.metadata.create_all(engine)

class SQLModelResourceRepository(ResourcesRepository):
  def all(self) -> list[Resource]:
    with Session(engine) as session:
      resource_models = session.exec(select(ResourceModel)).all()
    return [
       Resource(ResourceUrl(value=resource_model.url))
       for resource_model in resource_models
    ]

  def save(self, resource: Resource) -> None:
    resource_model = ResourceModel(url=resource.url().value)
    with Session(engine) as session:
       session.add(resource_model)
       session.commit()