#!/bin/sh
set -e  # Exit if any command fails

# Load environment variables
export $(grep -v '^#' /ws/.env | xargs)

# Run Hugo with the correct baseURL
exec hugo server --bind=0.0.0.0 --baseURL="$BASE_URL" --verbose --disableFastRender
