import unittest

from .utils import create_default_settings, settings_path
from sdg_settings import Settings

class TestSettings(unittest.TestCase):
    def setUp(self):
        self.settings = create_default_settings()

    def test_load_should_accept_single_path_string(self):
        self.settings.load(settings_path("config.json"))
        self.assertEqual(self.settings.PROJECT_DB_API_KEY, "123a")

    def test_load_should_accept_list_of_paths(self):
        self.settings.load([settings_path("config.json")])
        self.assertEqual(self.settings.PROJECT_DB_API_KEY, "123a")

    def test_load_should_load_settings_from_file(self):
        self.settings.load(settings_path("config.json"))
        self.assertEqual(self.settings.PROJECT_DB_API_KEY, "123a")
        self.assertEqual(self.settings.db_host, "foobar:8081")
        self.assertEqual(self.settings.LOG_LEVEL, "INFO")
        self.assertEqual(self.settings.MQ_HOST, "mq_test")
        self.assertEqual(self.settings.MQ_EXCHANGE, "km-test")
        self.assertEqual(self.settings.EXTRA_OPTION, "extra_option")

    def test_load_should_do_nothing_if_all_files_are_missing(self):
        self.settings.load(["not_exists_1.json", "not_exists_2.json"])
        self.assertEqual(self.settings, create_default_settings())

    def test_load_should_ignore_missing_files_and_load_only_existing_ones(self):
        self.settings.load(["not_exists_1.json", settings_path("config.json"), "not_exists_2.json"])
        self.assertEqual(self.settings.PROJECT_DB_API_KEY, "123a")
        self.assertEqual(self.settings.db_host, "foobar:8081")
        self.assertEqual(self.settings.LOG_LEVEL, "INFO")
        self.assertEqual(self.settings.MQ_HOST, "mq_test")
        self.assertEqual(self.settings.MQ_EXCHANGE, "km-test")
        self.assertEqual(self.settings.EXTRA_OPTION, "extra_option")

    def test_setting_should_be_accessible_with_upper_and_lower_case(self):
        self.assertEqual(self.settings.log_level, "ERROR")
        self.assertEqual(self.settings.LOG_LEVEL, "ERROR")

    def test_setting_should_be_accessible_by_property_and_key(self):
        self.assertEqual(self.settings["log_level"], "ERROR")
        self.assertEqual(self.settings.log_level, "ERROR")

    def test_loading_nested_object(self):
        self.settings.load([settings_path("nested_key.json")])
        self.assertEqual(self.settings.nested.depth, 1)

    def test_assinged_dict_to_property_should_become_instance_of_settings(self):
        self.settings.nested = { "depth": 1 }
        self.assertIsInstance(self.settings.nested, Settings)

    def test_assinged_dict_to_key_should_become_instance_of_settings(self):
        self.settings.nested = { "depth": 1 }
        self.assertIsInstance(self.settings.nested, Settings)


if __name__ == '__main__':
    unittest.main()
