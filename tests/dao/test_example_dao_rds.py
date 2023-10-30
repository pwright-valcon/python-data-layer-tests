from unittest import TestCase
from unittest.mock import patch, Mock
from dao.example_dao_rds import ExampleDAORDS


class ExampleDAORDSTests(TestCase):
    @patch('dao.example_dao_rds.psycopg2')
    def setUp(self, _mock_psycopg2):
        self.example_dao_rds = ExampleDAORDS({})

    @patch('dao.example_dao_rds.psycopg2')
    def test_connection_closed_on_success(self, _mock_psycopg2):
        self.example_dao_rds.select_one()

        self.assertTrue(self.example_dao_rds.db_connection.close.called)

    @patch('dao.example_dao_rds.psycopg2')
    def test_connection_closed_on_failure(self, _mock_psycopg2):
        self.example_dao_rds.db_connection.cursor.execute = Mock(side_effect=Exception('Test exception'))

        self.example_dao_rds.select_one()

        self.assertTrue(self.example_dao_rds.db_connection.close.called)
