FROM registry.redhat.io/ubi8/python-38:latest
RUN INSTALL_PKGS=git
RUN \
  python3 -m venv ${APP_ROOT} && \
  ${APP_ROOT}/bin/pip install --upgrade pip && \
  ${APP_ROOT}/bin/pip install GitPython PyYAML jinja2
COPY src /usr/src/site_defs_convert
WORKDIR /usr/src/site_defs_convert
CMD [ "python", "./site_defs_convert.py" ]