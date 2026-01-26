"""Streamlit entrypoint wrapper with lightweight dependency bootstrap."""

import subprocess
import sys
from pathlib import Path


def _ensure_deps():
    """Install requirements.txt if Streamlit is missing."""
    try:
        import streamlit  # type: ignore  # noqa: F401
    except ImportError:
        req = Path(__file__).parent / "requirements.txt"
        if req.exists():
            subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", str(req)])


def main():
    _ensure_deps()
    from app_streamlit import main as _main  # deferred import after deps installed

    _main()


if __name__ == "__main__":
    main()
