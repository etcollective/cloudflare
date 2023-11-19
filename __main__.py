import importlib
import os


def import_and_execute_functions(directory):
    """
    Imports Python modules from subdirectories and executes all callable functions in each module.

    Args:
    - directory (str): The path to the directory containing subdirectories with Python modules.

    Note:
    - This function assumes that each subdirectory in the specified directory contains Python modules
      (files with a '.py' extension) and skips the '__init__.py' file.
    - It imports each module and executes all callable functions found in the module.

    """
    for folder_name in os.listdir(directory):
        folder_path = os.path.join(directory, folder_name)
        if os.path.isdir(folder_path):
            module_names = [
                file_name[:-3]
                for file_name in os.listdir(folder_path)
                if file_name.endswith('.py') and file_name != '__init__.py'
            ]
            for module_name in module_names:
                module = importlib.import_module(
                    f'{folder_name}.{module_name}'
                )
                for func_name in dir(module):
                    if callable(getattr(module, func_name)):
                        getattr(module, func_name)()


if __name__ == '__main__':
    import_and_execute_functions('.')
