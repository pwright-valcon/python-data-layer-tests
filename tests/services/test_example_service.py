from unittest import TestCase
from unittest.mock import Mock
from services.example_service import ExampleService
from dao.interfaces.example_dao import ExampleDAO


class ExampleServiceTests(TestCase):
    def setUp(self):
        self.mock_dao = Mock(spec=ExampleDAO)
        self.example_service = ExampleService(self.mock_dao)

    def test_select_one_calls_dao(self):
        expected_value = '1'
        self.mock_dao.select_one = Mock(return_value=expected_value)

        result = self.example_service.select_one()

        self.assertEqual(result, expected_value)
