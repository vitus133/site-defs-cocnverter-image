# import git
import yaml
import json
from jinja2 import Template
from munch import Munch
import configparser



if __name__ == "__main__":
  config = configparser.ConfigParser()
  config.read('ini/ClusterDeployment.ini')
  deployment = Munch.fromDict(config)
  with open('ini/authorized_keys', 'r') as ak:
    auth_keys = ak.read()
  # print(json.dumps(deployment, indent=2))
  with open('templates/infra_env.yaml.j2', 'r') as tf:
    infra_env_str = tf.read()
  infra_env = Template(infra_env_str)
  # print(infra_env.render(
  #   deployment=deployment, ssh_auth_keys_str=auth_keys))
  cd = yaml.safe_load(infra_env.render(
    deployment=deployment, ssh_auth_keys_str=auth_keys))
  print(yaml.dump(cd))

