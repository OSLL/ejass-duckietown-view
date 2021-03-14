FROM python:3.8-slim-buster

WORKDIR .

COPY scripts scripts/
COPY requirements.txt requirements.txt

# APT
RUN bash ./scripts/install_dev.sh

# PIP
RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]