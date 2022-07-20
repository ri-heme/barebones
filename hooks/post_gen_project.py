from pathlib import Path

module_name = "{{cookiecutter.project_slug}}"
use_hydra = int("{{cookiecutter.hydra}}")

# Delete MANIFEST and config module if not using Hydra
if not use_hydra:
    manifest_file = Path.cwd() / "MANIFEST.in"
    manifest_file.unlink()
    config_file = Path.cwd() / "src" / module_name / "conf/__init__.py"
    config_file.unlink()
    config_file.parent.rmdir()
