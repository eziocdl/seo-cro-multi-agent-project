#!/usr/bin/env bash
set -e

echo "[START] Starting gunicorn server on port $PORT..."
echo "[START] Configuration: 1 worker, 4 threads, 180s timeout"

# Start gunicorn - removed --preload to avoid startup issues
exec gunicorn app:app \
  --bind 0.0.0.0:$PORT \
  --timeout 180 \
  --workers 1 \
  --threads 4 \
  --worker-class gthread \
  --log-level debug \
  --access-logfile - \
  --error-logfile - \
  --capture-output \
  --enable-stdio-inheritance
