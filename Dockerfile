# FROM registry.redhat.io/ubi8/python-38:latest
FROM quay.io/centos/centos:latest
RUN yum -y install git vim python3 python3-pip python3-devel python3-virtualenv
RUN \
  export APP_ROOT=/usr/src && \
  python3 -m venv ${APP_ROOT}/venv && \
  ${APP_ROOT}/venv/bin/pip3 install --upgrade pip && \
  ${APP_ROOT}/venv/bin/pip3 install GitPython PyYAML jinja2 munch && \
  ssh-keygen -b 4096 -t rsa -f /root/.ssh/id_rsa -q -N ""
COPY src /usr/src/site_defs_convert
WORKDIR /usr/src/site_defs_convert
ENTRYPOINT ["/bin/bash", "-c", "/usr/src/site_defs_convert/entrypoint.sh"]
