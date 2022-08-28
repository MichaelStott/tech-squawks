""" Helper functions for CI/CD process.
"""

import os
from pathlib import Path
from pydoc import Helper

import click, git

class CIHelper():
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
        changes = self._get_changed_files()
        for change in changes:
            if change.startswith("web/"):
                result = True
                break
        return result

    def _get_changed_files(self):
        """ Get list of files that changed in branch.
        """
        repo = git.Repo(".", search_parent_directories=True)
        changes = [ item.a_path for item in repo.index.diff("main") ]
        return(changes)

@click.group()
def main():
    pass

@main.group()
def web():
    pass

@main.group()
def code():
    pass

@web.command("has-changed")
def has_changed():
    helper = CIHelper()
    click.echo(helper.website_updated())

@code.command("ls")
def has_changed():
    helper = CIHelper()
    click.echo(helper.get_pulumi_projects())

if __name__ == "__main__":
    main()
