FROM python:3.7
ADD . /movi-eeze-flask
WORKDIR /movi-eeze-flask
RUN pip install -r requirements.txt
CMD bash movi-eeze-flask/run-flask.sh
