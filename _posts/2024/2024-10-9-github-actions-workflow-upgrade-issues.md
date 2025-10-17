---
description: "Learn how to efficiently update GitHub Actions in your workflows with a Python script that automatically checks for newer versions, helping you maintain compatibility with current Node.js runtimes and keep your CI/CD processes running smoothly."
excerpt_separator: <!--more-->
layout: post
tags: github python
categories: [Tools and Platforms]
title: "Easy Way to Upgrade Actions Used in Your GitHub Actions Workflow"
---
No doubt I use GitHub Actions a lot in my projects, and I have workflows that are created a long time ago. As GitHub Actions evolves, especially when the Node.js runtime used by many actions became obsolete, I have to upgrade the actions to newer versions so that the workflows can continue to run without issues.
<!--more-->

## The Problem

The problem is that I have to manually check the actions used in my workflows and then visit the GitHub Marketplace to find the latest versions. This is a tedious process, and I wish there is an easier way to do this.

## The Solution

I found a way to automate this process, and it is quite simple by simply asking ChatGPT o1. And it kindly gave me this script file,

``` python
import re
import requests
import yaml
import sys

GITHUB_API_URL = "https://api.github.com/repos/{owner}/{repo}/releases/latest"

def get_latest_version(owner, repo):
    try:
        response = requests.get(GITHUB_API_URL.format(owner=owner, repo=repo))
        response.raise_for_status()
        data = response.json()
        return data.get("tag_name", "Unknown")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching latest version for {owner}/{repo}: {e}")
        return "Unknown"

def parse_workflow_file(workflow_file_path):
    with open(workflow_file_path, 'r') as file:
        try:
            workflow = yaml.safe_load(file)
        except yaml.YAMLError as e:
            print(f"Error parsing YAML file: {e}")
            return []

    actions = []
    jobs = workflow.get('jobs', {})
    for job in jobs.values():
        steps = job.get('steps', [])
        for step in steps:
            if 'uses' in step:
                uses_value = step['uses']
                match = re.match(r'([^@]+)@(.+)', uses_value)
                if match:
                    action = match.group(1)
                    version = match.group(2)
                    actions.append((action, version))
    return actions

def main(workflow_file_path):
    actions = parse_workflow_file(workflow_file_path)
    
    for action, current_version in actions:
        owner_repo = action.replace('https://github.com/', '').split('/')
        if len(owner_repo) == 2:
            owner, repo = owner_repo
            latest_version = get_latest_version(owner, repo)
            if latest_version == "Unknown":
                print(f"Could not determine the latest version for {action}")
            elif current_version != latest_version:
                print(f"Action {action}: Current version {current_version} is not the latest. Latest version is {latest_version}.")
            else:
                print(f"Action {action}: Current version {current_version} is the latest.")
        else:
            print(f"Skipping unsupported action format: {action}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python validate_action_versions.py <workflow_file_path>")
        sys.exit(1)

    workflow_file_path = sys.argv[1]
    main(workflow_file_path)
```

This script is quite simple, it reads a GitHub Actions workflow file, extracts the actions used in the workflow, and then checks the latest version of the actions using the GitHub API. If the action is outdated, it will print a message to inform you.

## How to Use

So when I ran it against one of my workflows, it showed me the actions that are outdated,

``` bash
$ python validate_action_versions.py .github/workflows/build.yml
Action actions/checkout: Current version v2 is not the latest. Latest version is v4.2.1.
Action actions/setup-dotnet: Current version v1 is not the latest. Latest version is v4.0.1.
Action actions/checkout: Current version v2 is not the latest. Latest version is v4.2.1.
Action actions/setup-dotnet: Current version v1 is not the latest. Latest version is v4.0.1.
Action actions/checkout: Current version v2 is not the latest. Latest version is v4.2.1.
Action actions/setup-dotnet: Current version v1 is not the latest. Latest version is v4.0.1.
Action coverallsapp/github-action: Current version master is not the latest. Latest version is v2.3.0.
```

Clearly it saves me a lot of time and I don't need to search for latest versions of the tasks on my own.

## Conclusion

ChatGPT o1 has been out for a while now, and people can use it t generate many useful scripts like this one. I hope you find this script useful and can use it in your projects as well.
