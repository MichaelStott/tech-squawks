
class PulumiEnumerator():

    def __init__(self):
        self.project_list_file = "pulumi_project_list.txt"

    def get_pulumi_projects(self):
        results = []
        with open(self.project_list_file) as project_file:
            for line in project_file:
                if line:
                    results.append(line)
        return results

if __name__ == "__main__":
    pulumi_enum = PulumiEnumerator()
    projects = pulumi_enum.get_pulumi_projects()
    print(projects)
