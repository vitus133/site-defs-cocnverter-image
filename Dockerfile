# FROM registry.redhat.io/ubi8/python-38:latest
FROM quay.io/centos/centos:latest
RUN yum -y install git python3 python3-pip python3-devel python3-virtualenv
RUN \
  export APP_ROOT=/usr/src && \
  python3 -m venv ${APP_ROOT}/venv && \
  ${APP_ROOT}/venv/bin/pip3 install --upgrade pip && \
  ${APP_ROOT}/venv/bin/pip3 install GitPython PyYAML jinja2 munch
COPY src /usr/src/site_defs_convert
WORKDIR /usr/src/site_defs_convert
CMD [ "${APP_ROOT}/venv/bin/python3", "./site_defs_convert.py" ]