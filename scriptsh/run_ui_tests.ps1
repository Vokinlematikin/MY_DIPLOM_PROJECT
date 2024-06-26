#!/bin/bash
#cd ..
#ls
#pytest -v -s ./page_test/tests/test_main_page.py --alluredir=results
cd D:\PYCHARM\QA1023\MY_DIPLOM_PROJECT\venv\Scripts\Activate.ps1
python -m pytest --alluredir D:\PYCHARM\QA1023\MY_DIPLOM_PROJECT\results
pytest -v -s "D:\PYCHARM\QA1023\MY_DIPLOM_PROJECT\tests"

# Получаем текущую директорию скрипта
SCRIPT_DIR=$(dirname "$0")
pwd

# Определяем путь к тестовому файлу относительно директории со скриптом
TEST_FILE="$SCRIPT_DIR/../tests/test_main_page.py"

# Определяем путь к директории с отчетами относительно директории со скриптом
REPORT_DIR="$SCRIPT_DIR/../results"

# Запускаем pytest с использованием относительного пути к файлу test_main_page.py и директории с отчетами
pytest -v -s "$TEST_FILE" --alluredir="$REPORT_DIR"