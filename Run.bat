pytest -v -s -m "regression" --html=./Reports/report.html testCases --capture=tee-sys
REM pytest -v -s -m "sanity and regression" --html=./Reports/report.html testCases --capture=tee-sys
REM pytest -v -s -m "sanity or regression" --html=./Reports/report.html testCases --capture=tee-sys
REM pytest -v -s -m "sanity" --html=./Reports/report.html testCases --capture=tee-sys

