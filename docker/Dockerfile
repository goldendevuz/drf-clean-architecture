FROM python:3.13-slim

# environment variables
ARG DJANGO_ENV
ENV DJANGO_ENV=$DJANGO_ENV \
    PROJECT_DIR="/code" \
    PYTHONFAULTHANDLER=1 \
    PYTHONHASHSEED=random \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    POETRY_VERSION=2.2.1 \
    POETRY_VIRTUALENVS_CREATE=false \
    PATH="${PATH}:/root/.local/bin"

# system dependencies
RUN apt-get update && apt-get upgrade -y \
    && apt-get install --no-install-recommends --no-install-suggests -y \
       build-essential \
       libpq-dev \
       postgresql \
       postgresql-contrib \
       python3-dev \
       curl \
    && apt-get autoremove -y && apt-get clean -y && rm -rf /var/lib/apt/lists/* \
    \
    # ensure pip and required Python packages
    && python3 -m ensurepip \
    && python3 -m pip install --upgrade pip setuptools wheel six \
    \
    # install Poetry 2.2.1 via official installer
    && curl -sSL https://install.python-poetry.org | python3 - --version $POETRY_VERSION \
    && poetry --version

# set working directory
WORKDIR $PROJECT_DIR

# copy scripts as entry points
COPY ./scripts ${PROJECT_DIR}/scripts/

# copy only dependency files
COPY ./pyproject.toml ./poetry.lock ${PROJECT_DIR}/

# setting up proper permissions
RUN chmod +x ${PROJECT_DIR}/scripts/entrypoint.sh \
    && chmod +x ${PROJECT_DIR}/scripts/start_api.sh \
    && chmod +x ${PROJECT_DIR}/scripts/start_worker.sh \
    && groupadd -r api && useradd -d /code -r -g api api \
    && chown api:api -R /code

# install dependencies (without trying to install the root project)
RUN poetry config virtualenvs.create false \
    && poetry install --no-root $(test "$DJANGO_ENV" = production && echo "--no-dev") --no-interaction --no-ansi

# expose port
EXPOSE $PORT

# copy full project
COPY --chown=api:api . ${PROJECT_DIR}/

# run as non-root user
USER api

# entrypoint
CMD ./scripts/entrypoint.sh
