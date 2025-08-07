import pytest
from sqlmodel import SQLModel, Session, select
from resources.domain.models import Resource
from resources.domain.value_objects import ResourceUrl
from resources.infrastructure.repositories import ResourceModel, SQLModelResourceRepository, engine


class TestSQLModelResourceRepository:
  @pytest.fixture(autouse=True)
  def cleanup_database(self):
    yield
    SQLModel.metadata.drop_all(engine)

  def test_saves_resource_to_database(self) -> None:
    repo = SQLModelResourceRepository()

    repo.save(Resource(ResourceUrl(value="http://google.com")))

    with Session(engine) as session:
      statement = select(ResourceModel)
      resource = session.exec(statement).first()
      resource.url = "http://google.com"