import os


class HelperSystem:
    def get_project_dir(self):
        current_dir = os.path.abspath(os.path.dirname(__file__))
        while not os.path.isfile(os.path.join(current_dir, 'conftest.py')):
            parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))
            if parent_dir == current_dir:
                raise Exception("could not find project root directory.")
            current_dir = parent_dir
        return current_dir
