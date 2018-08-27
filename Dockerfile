FROM python:3.7-alpine

RUN apk add --update --no-cache g++ gcc libxslt-dev

WORKDIR /mini_readability


COPY requirements.txt ./
COPY test-requirements.txt ./
RUN pip install -r requirements.txt -r test-requirements.txt

COPY . .

WORKDIR /mini_readability/mini_readability/src/

ENTRYPOINT ["python", "-m", "mini_readability.main"]
