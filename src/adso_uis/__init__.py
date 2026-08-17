"""Compatibility package to satisfy builders expecting `src/adso_uis`.

This module delegates a simple `main()` to `app.main.main` so the project
can be installed when the build backend expects a package named after the
normalized project name (`ADSO-UIS` -> `adso_uis`).
"""

def main(*args, **kwargs):
    from app.main import main as _app_main
    return _app_main(*args, **kwargs)

__all__ = ["main"]
