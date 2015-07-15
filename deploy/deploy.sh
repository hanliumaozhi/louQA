#!/bin/bash

/home/han/QA/venv/bin/supervisorctl -c  /home/han/QA/deploy/supervisor/supervisord.conf stop QA
kill -9 `ps -ef|grep gunicorn|grep -v grep|awk '{print $2}'`
/home/han/QA/venv/bin/supervisorctl -c  /home/han/QA/deploy/supervisor/supervisord.conf start QA

