# import git
import yaml
# import json
import os
from time import gmtime, strftime
import shutil
from jinja2 import Template
from munch import Munch
import configparser
from git import Git, Repo



if __name__ == "__main__":
  config = configparser.ConfigParser()
  config.read('ini/ClusterDeployment.ini')
  deployment = Munch.fromDict(config)
  with open('ini/authorized_keys', 'r') as ak:
    auth_keys = ak.read().split('\n')
  # print(json.dumps(deployment, indent=2))
  with open('templates/infra_env.yaml.j2', 'r') as tf:
    infra_env_str = tf.read()
  infra_env = Template(infra_env_str)
  print(infra_env.render(
    deployment=deployment, ssh_auth_keys=auth_keys))
  cd = yaml.safe_load(infra_env.render(
    deployment=deployment, ssh_auth_keys=auth_keys))
  print(yaml.dump(cd))

  shutil.rmtree('installmanifests', ignore_errors=True)
  commit_msg = f"Convert format: {strftime('%a, %d %b %Y %H:%M:%S +0000', gmtime())}"

  # clone the repo
  git_ssh_identity_file = os.path.join('secrets', 'target_repo_private_key')
  git_ssh_cmd = 'ssh -i %s' % git_ssh_identity_file
  repo = Repo.clone_from(
    'git@gitlab.com:vtalikgr/installmanifests.git',
    'installmanifests',
    branch='main',
    depth=1)
  with open('installmanifests/infra_env.yaml', 'w') as ie:
    yaml.dump(cd, ie)
  repo.git.add('infra_env.yaml')
  repo.git.commit('-a', '-m', commit_msg, author='vitus@dr.com')
  
  repo.git.push('origin', 'main')