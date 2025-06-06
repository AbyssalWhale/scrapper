import json
import os

from enums.framework.enums_framework_config_properties import EnumsFrameworkConfigProperties
from helpers.helper_system import HelperSystem


class HelperRunConfig:
    def __init__(self, system_helper: HelperSystem):
        self._system_helper = system_helper
        self._config = self._get_config()
        self._set_all_dirs()

    def get_property_value(self, property_name: EnumsFrameworkConfigProperties):
        return self._config[str(property_name.value)]

    def _set_all_dirs(self):
        self._set_data_dir()

    def _set_data_dir(self):
        try:
            tests_result_dir_path = os.path.join(
                self._system_helper.get_project_dir(),
                self.get_property_value(property_name=EnumsFrameworkConfigProperties.DIR_DATA)
            )
            self._config[EnumsFrameworkConfigProperties.DIR_DATA.value] = tests_result_dir_path
            os.makedirs(tests_result_dir_path, exist_ok=True)
        except OSError as ex:
            raise RuntimeError(f"unable to create data directory: {ex}") from ex
        except Exception as ex:
            raise RuntimeError(f"unexpected error while setting data dir: {ex}") from ex

    def _get_config(self):
        file_name = "config.json"
        full_file_path = os.path.join(
            self._system_helper.get_project_dir(),
            file_name)
        if os.path.exists(full_file_path):
            with open(full_file_path) as f:
                result = json.load(f)
                return result
        else:
            raise Exception(f"could not find test run config: {file_name}. Path: {full_file_path}")