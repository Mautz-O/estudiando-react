#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

BACKEND_DIR="$ROOT_DIR/backend"
FRONTEND_DIR="$ROOT_DIR/frontend"
VENV_DIR="$BACKEND_DIR/.venv"

# ==========================================
# Buscar Python
# ==========================================
function find_python() {
  if command -v python >/dev/null 2>&1; then
    echo python
  elif command -v python3 >/dev/null 2>&1; then
    echo python3
  else
    echo "ERROR: Python no encontrado en PATH." >&2
    exit 1
  fi
}

PYTHON_BIN="$(find_python)"

# ==========================================
# Comprobar entorno virtual
# ==========================================
if [ ! -d "$VENV_DIR" ]; then
  echo "ERROR: No existe el entorno virtual:"
  echo "$VENV_DIR"
  echo ""
  echo "Créalo con:"
  echo "cd backend"
  echo "python -m venv .venv"
  exit 1
fi

# ==========================================
# Activar entorno virtual
# ==========================================
if [ -f "$VENV_DIR/Scripts/activate" ]; then
  source "$VENV_DIR/Scripts/activate"
elif [ -f "$VENV_DIR/bin/activate" ]; then
  source "$VENV_DIR/bin/activate"
else
  echo "ERROR: No se encontró el script de activación." >&2
  exit 1
fi

# ==========================================
# Python del entorno virtual
# ==========================================
PYTHON_VENV="$VENV_DIR/Scripts/python.exe"
if [ ! -f "$PYTHON_VENV" ]; then
  PYTHON_VENV="$VENV_DIR/bin/python"
fi

echo ""
echo "=========================================="
echo "Entorno virtual:"
echo "$VENV_DIR"
echo ""
echo "Python:"
"$PYTHON_VENV" -c "import sys; print(sys.executable)"
echo "=========================================="
echo ""

# ==========================================
# Detener servicios
# ==========================================
function cleanup() {
  if [ -n "${BACKEND_PID:-}" ]; then
    echo ""
    echo "Deteniendo FastAPI..."
    kill "$BACKEND_PID" 2>/dev/null || true
  fi
}

trap cleanup EXIT INT TERM

# ==========================================
# Iniciar FastAPI
# ==========================================
echo "Iniciando FastAPI..."

pushd "$BACKEND_DIR" >/dev/null

"$PYTHON_VENV" -m uvicorn modules.IA_services:app --reload --host 127.0.0.1 --port 8000 &
BACKEND_PID=$!

popd >/dev/null

# ==========================================
# Iniciar React
# ==========================================
echo ""
echo "Iniciando React..."

pushd "$FRONTEND_DIR" >/dev/null

npm run dev

popd >/dev/null
