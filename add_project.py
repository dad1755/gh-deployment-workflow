# add_project.py
import json
import os
import argparse

def add_project(tag, title, description, stats, code=None):
    file_path = 'projects.json'
    projects = []

    # Read existing projects
    if os.path.exists(file_path):
        try:
            with open(file_path, 'r') as f:
                projects = json.load(f)
        except json.JSONDecodeError:
            print(f"Error: '{file_path}' is corrupted or invalid JSON. Starting with an empty project list.")
            projects = []

    # Check for duplicate title
    for project in projects:
        if project['title'].lower() == title.lower():
            print(f"Project '{title}' already exists. Updating...")
            project.update({
                'tag': tag,
                'title': title,
                'description': description,
                'stats': stats,
                'code': code
            })
            break
    else:
        # Add new project
        projects.append({
            'tag': tag,
            'title': title,
            'description': description,
            'stats': stats,
            'code': code
        })

    # Write back to projects.json
    try:
        with open(file_path, 'w') as f:
            json.dump(projects, f, indent=2)
        print(f"[✓] Project '{title}' added/updated in {file_path}")
    except Exception as e:
        print(f"Error writing to '{file_path}': {e}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Add or update a project in projects.json")
    parser.add_argument('--tag', required=True, help="Project tag (e.g., Monitoring, CI/CD)")
    parser.add_argument('--title', required=True, help="Project title")
    parser.add_argument('--description', required=True, help="Project description")
    parser.add_argument('--stats', required=True, help="Project stats (e.g., 600)")
    parser.add_argument('--code', help="Optional code snippet for the project")

    args = parser.parse_args()

    add_project(args.tag, args.title, args.description, args.stats, args.code)
