# Build container stage
FROM docker.io/library/ubuntu:24.04 AS build

ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install --no-install-recommends -y \
    make \
    python3-pip \
    pandoc \
    wkhtmltopdf \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /site
COPY requirements.txt /site

RUN pip install --no-cache-dir --break-system-packages -r requirements.txt

COPY . /site
ARG CI_PROJECT_PATH
ARG CI_PROJECT_URL
ARG CI_COMMIT_SHORT_SHA
ARG CI_COMMIT_SHA
ARG CI_PIPELINE_ID
ARG CI_PIPELINE_URL
RUN make

FROM docker.io/p3terx/darkhttpd:1.16

WORKDIR /public

COPY --from=build /site/out /public

EXPOSE 80

CMD ["/public"]
