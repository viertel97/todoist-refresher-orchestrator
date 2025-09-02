FROM python:3.11-slim-bookworm

ARG PAT

RUN apt-get update && apt-get upgrade -y && apt-get install -y procps

COPY . .

COPY requirements.txt .

RUN pip install -r requirements.txt
RUN pip install --upgrade --extra-index-url https://Quarter-Lib-Old:${PAT}@pkgs.dev.azure.com/viertel/Quarter-Lib-Old/_packaging/Quarter-Lib-Old/pypi/simple/ quarter-lib-old

ENV IS_CONTAINER=True

CMD ["python", "main.py"]
