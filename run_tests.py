
import subprocess
import sys
import platform
import shutil
from pathlib import Path

import django


BASE_DIR = Path(__file__).resolve().parent
RESULTS_DIR = BASE_DIR / "allure-results"
REPORT_DIR = BASE_DIR / "allure-report"


def main():
    allure_cli = shutil.which("allure")

    if not allure_cli:
        sys.exit("Allure CLI is not installed or not in PATH.")

    # Run all tests
    result = subprocess.run(
        [sys.executable, "-m", "pytest"],
        cwd=BASE_DIR
    )

    # Check test execution
    if result.returncode not in (0, 1):
        sys.exit(result.returncode)

    # Add environment information
    RESULTS_DIR.mkdir(exist_ok=True)

    environment = (
        "Project=py-django-testcase\n"
        f"Python={platform.python_version()}\n"
        f"Django={django.get_version()}\n"
        f"OS={platform.system()}\n"
        "Environment=Local\n"
        "Database=SQLite\n"
    )

    (RESULTS_DIR / "environment.properties").write_text(
        environment, encoding="utf-8"
    )

    # Generate Allure report
    subprocess.run(
        [
            allure_cli,
            "generate",
            str(RESULTS_DIR),
            "-o",
            str(REPORT_DIR),
            "--clean"
        ],
        check=True
    )

    # Open Allure report
    subprocess.run(
        [allure_cli, "open", str(REPORT_DIR)],
        check=True
    )

    sys.exit(result.returncode)


if __name__ == "__main__":
    main()
