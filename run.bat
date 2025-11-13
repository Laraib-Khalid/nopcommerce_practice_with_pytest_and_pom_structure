echo off
call venv/scripts/activate
pytest -s -rA -v --html=reports/test_report.html --self-contained-html test_cases/test_add_customer_user.py
pause