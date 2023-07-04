#!/usr/bin/python3
"""
Lists 10 commits from recent to oldest from GitHub repository
"""
import sys
import requests

if __name__ == "__main__":
    repo = sys.argv[1]
    user = sys.argv[2]

    # Construct URL for GitHub API endpoint
    url = f"https://api.github.com/repos/{user}/{repo}/commits"
    params = {"per_page": 10, "sort": "author-date", "order": "desc"}
    response = requests.get(url, params=params)
    if response.status_code == 200:
        commits = response.json()

        # Iterate over the list of commits
        for commit in commits:
            sha = commit["sha"]
            author_name = commit["commit"]["author"]["name"]
            print(f"{sha}: {author_name}")
