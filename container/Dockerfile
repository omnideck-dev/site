FROM python:3.12-slim-bookworm AS build

WORKDIR /site
COPY . .

RUN bash scripts/sync-data.sh \
    && ./arbor check \
    && ./arbor build

FROM scratch

COPY --from=build /site/public/ /
