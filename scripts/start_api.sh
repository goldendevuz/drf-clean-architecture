#!/usr/bin/bash

set -o errexit
set -o nounset

# Check env variables
echo "DJANGO_ENV is ${DJANGO_ENV}"
echo "Port ${DJANGO_PORT} exposed for Forex API"

# Set working directory
cd ${PROJECT_DIR}
echo "Change to working directory $(pwd)"

# Run database migrations
python manage.py makemigrations
python manage.py migrate
python manage.py migrate --fake

# echo "Collecting static files..."
# python manage.py collectstatic --noinput

if [ ${DJANGO_ENV} = 'development' ]; then
    # Create superuser if not exists
    export DJANGO_SUPERUSER_USERNAME="admin"
    export DJANGO_SUPERUSER_PASSWORD="admin"
    export DJANGO_SUPERUSER_EMAIL="admin@forex.com"
    python manage.py createsuperuser --noinput || echo "Superuser already exists."

    FIXTURE_DIR="$PROJECT_DIR/fixtures"

    # Load all fixtures if present
    for file in $FIXTURE_DIR/*.json; do
        # Skip loop if no files found
        [ -e "$file" ] || continue

        echo "Loading fixture: $file"
        python manage.py loaddata "$file"
    done

fi

# Start API server
echo "Starting Uvicorn ASGI server..."
uvicorn src.infrastructure.server.asgi:application --host 0.0.0.0 --port ${DJANGO_PORT}