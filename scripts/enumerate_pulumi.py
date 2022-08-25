""" Script used by CI/CD process to determine which directories to test.
"""

import os
from pathlib import Path

class PulumiEnumerator():

    DEFAULT_PROJECT_DIR = "code"

    def __init__(self):
        """ Initialize enumerators. Determine which directories to test.
        """
        self.project_dir = os.getenv("PROJECT_DIR", self.DEFAULT_PROJECT_DIR)
        self.blacklisted = self._get_ignore_dirs()
        
    def _get_ignore_dirs(self):
        """ Determine which directories to ignore.
        """
        blacklisted = os.getenv("BLACKLISTED_DIRS", "")
        return [x.strip() for x in blacklisted.split(",")]

    def get_pulumi_projects(self):
        """ Get Pulumi project directories.
        """
        results = set()
        for path in Path(self.project_dir).rglob('Pulumi.*.yaml'):
            path_str = str(path.parent)
            if "node_modules" not in path_str:
                results.add(path_str)
        return list(results)

if __name__ == "__main__":
    pulumi_enum = PulumiEnumerator()
    projects = pulumi_enum.get_pulumi_projects()
    print(projects)
