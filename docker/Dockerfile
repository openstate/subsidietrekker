FROM python:2.7.12

WORKDIR /opt/subsidietrekker
RUN pip install \
  wsgiref==0.1.2 \
  dominate==2.2.0 \
  elasticsearch==2.3.0 \
  Flask \
  Flask-WTF==0.12 \
  flask-cors==2.1.2 \
  itsdangerous==0.24 \
  Jinja2==2.8 \
  MarkupSafe==0.23 \
  requests==2.9.1 \
  urllib3==1.14 \
  visitor==0.1.2 \
  Werkzeug==0.11.4 \
  WTForms==2.1 \
  uwsgi

# Production
# CMD uwsgi --socket 0.0.0.0:5000 -w main:main_app

# Development
ENV FLASK_APP=main.py \
   FLASK_DEBUG=1
CMD flask run --host=0.0.0.0
