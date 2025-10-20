#!/bin/bash

case "$1" in
  dev)
    export ENV=local
    echo "🚀 Starting FastAPI in DEV mode..."
    uvicorn app.main:app --reload
    ;;
  prod)
    export ENV=prod
    echo "🚀 Starting FastAPI in PROD mode (detached with nohup)..."
    nohup uvicorn app.main:app --host 0.0.0.0 --port 8000 > fastapi.log 2>&1 &
    echo "✅ FastAPI is running in the background (log: fastapi.log)"
    ;;
  stop)
    echo "🛑 Stopping FastAPI..."
    pkill -f "uvicorn app.main:app"
    ;;
  *)
    echo "Usage: ./run.sh [dev|prod|stop]"
    ;;
esac
