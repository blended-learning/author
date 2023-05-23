#!/usr/bin/env python

import json
from pprint import pprint
import os
import git

def get_token(value):
    if value is None:
        return os.environ.get('GITHUB_TOKEN')
    elif value.startswith('$'):
        return os.environ.get(value[1:])
    else:
        return value
    
def get_clone_url(github_user, token, repo):
    if github_user and token:
        return f'https://{github_user}:{token}@github.com/{repo}'
    elif github_user:
        return f'https://{github_user}@github.com/{repo}'
    else:
        return f'https://github.com/{repo}'
    
def clone(git_url, target):
    if os.path.exists(target):
        print(f'"{target}" already exists.')
        return None
    else:
        repo = "/".join(git_url.split("/")[-2:])
        directory = "/".join(target.split("/")[-2:])
        print(f'Cloning "{repo}" into "{directory}"')
        return git.Repo.clone_from(git_url, target)

def main(repos_json_filename, username=None):
    username = username or os.environ['USER']
    HOME = os.environ['HOME']
    with open(repos_json_filename, 'r') as f:
        repos_config = json.load(f)
        user_repos = repos_config.get(username)
        if user_repos:
            token = get_token(user_repos.get('token'))
            github_user = user_repos.get('github_user')
            for repo_name in user_repos['repos']:
                repo_name = repo_name.strip('/')
                url = get_clone_url(github_user, token, repo_name)
                target = os.path.join(f'{HOME}/github/{repo_name}')
                repo = clone(url, target)
                if repo:
                    repo.config_writer().set_value("user", "name", username).release()
                    repo.config_writer().set_value("user", "email", f"{username}@docker").release()

if __name__ == '__main__':
    import sys
    if len(sys.argv[1:]) == 2:
        file, username = sys.argv[1:3]
    elif len(sys.argv[1:]) == 1:
        file, username = sys.argv[1], None
    else:
        file, username = '/etc/repos.json', None
    main(file, username)