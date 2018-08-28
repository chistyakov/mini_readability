FROM python:3.7-alpine

RUN apk add --update --no-cache g++ gcc libxslt-dev

WORKDIR /mini_readability


COPY requirements.txt ./
COPY test-requirements.txt ./
RUN pip install -r requirements.txt -r test-requirements.txt

ENV PARSE_CONFIG_PATH /mini_readability/config.yaml
ENV TLDEXTRACT_CACHE /tmp/tldextract.cache
ENV OUTPUT_BASE_PATH /data
ENV SAMPLES_BASE_PATH /mini_readability/mini_readability/tests/samples

COPY . .

WORKDIR /mini_readability/mini_readability/src/

ENTRYPOINT ["python", "-m", "mini_readability.main"]
