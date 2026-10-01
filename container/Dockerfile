FROM python:3.12-slim-bookworm AS build

WORKDIR /site
COPY . .

RUN python3 -m unittest discover -s tests -v \
    && bash scripts/sync-data.sh \
    && ./arbor check \
    && ./arbor build \
    && python3 scripts/verify-site.py public

FROM scratch

COPY --from=build /site/public/ /
