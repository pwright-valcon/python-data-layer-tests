from services.example_service import ExampleService
from dao.example_dao_rds import ExampleDAORDS
from config import example_rds_db_config


def select_one():
    example_dao = ExampleDAORDS(example_rds_db_config)
    example_service = ExampleService(example_dao)
    return example_service.select_one()


if __name__ == '__main__':
    result = select_one()
    print(result)
