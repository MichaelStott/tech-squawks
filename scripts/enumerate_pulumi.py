""" Helper functions for CI/CD process.
"""

import os
from pathlib import Path

from git import Repo

class TSHelper():
    """ Helper class for all CI/CD operations.
    """

    DEFAULT_PROJECT_DIR = "code"

    def __init__(self):
        """ Initialize enumerators. Determine which directories to test.
        """
        self.project_dir = os.getenv("PROJECT_DIR", self.DEFAULT_PROJECT_DIR)
        self.blacklisted = self._get_ignore_dirs()
        self.ts_repo = os.getenv("REPO_ROOT_DIR", ".")
        
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

    def website_updated(self):
        """ Determine if website has been updated
        """
        result = False
        return result

    def git_diff(self, branch_a, branch_b):
        """ Check if git 
        """
        pass

if __name__ == "__main__":
    pulumi_enum = PulumiEnumerator()
    projects = pulumi_enum.get_pulumi_projects()
    print(projects)
