#!/bin/bash

set -euo pipefail

CURRENT_GIT_BRANCH="$(git rev-parse --abbrev-ref HEAD)"

print_start_time() {
    echo ""; echo "--- Started at $(date +"%d-%m-%Y %T")"; echo ""
}

print_finish_time() {
    echo ""; echo "--- Finished at $(date +"%d-%m-%Y %T")"; echo ""
}

TEST_REPORT_FILE="."
delete_the_old_test_report() {
    TEST_REPORTS_FOLDER=".test-run-reports"
    mkdir -p "${TEST_REPORTS_FOLDER}"
    TEST_REPORT_FILE="${TEST_REPORTS_FOLDER}/test-report-${CURRENT_GIT_BRANCH}.html"
    rm -f ${TEST_REPORT_FILE} && echo "Deleting old test report file: ${TEST_REPORT_FILE}"
}

COVERAGE_REPORT_FOLDER=".coverage-reports"
COVERAGE_REPORT_FILE=""
delete_the_old_coverage_report_folder_and_create_a_new_one() {
    mkdir -p "${COVERAGE_REPORT_FOLDER}"
    COVERAGE_REPORT_FOLDER="${COVERAGE_REPORT_FOLDER}/coverage-report-${CURRENT_GIT_BRANCH}"
    rm -fr ${COVERAGE_REPORT_FOLDER} && echo "Deleting old test coverage folder: ${COVERAGE_REPORT_FOLDER}"
    COVERAGE_REPORT_FILE="${COVERAGE_REPORT_FOLDER}/index.html"
    rm -f .coverage.*
}

test_for_pytest(){
  result="python -m pytest"
  exit_code=0
  TMPFILE=$(mktemp)
  pytest 2&> ${TMPFILE} || exit_code="$?" && true
  rm -f ${TMPFILE}
  if [[ ${exit_code} == 0 ]]; then
     result="pytest"
  fi
  echo ${result}
}

test_run_exit_code=0
SOURCES_FOLDER=nlp_profiler
TESTS_FOLDER=tests
TARGET_TEST_FOLDERS="$@"
TARGET_TEST_FOLDERS="${TARGET_TEST_FOLDERS:-${TESTS_FOLDER}}"
RUN_PYTEST=$(test_for_pytest)
run_test_runner() {
    echo ""; echo "~~~ Running tests with coverage on branch '${CURRENT_GIT_BRANCH}'"
    set -x
    ${RUN_PYTEST} --cov-config pyproject.toml             \
           --cov-report html:"${COVERAGE_REPORT_FOLDER}"  \
           --cov=${SOURCES_FOLDER} ${TARGET_TEST_FOLDERS} \
          --html="${TEST_REPORT_FILE}"                   \
          || test_run_exit_code="$?" && true
    set +x
    echo ""; echo "~~~ The test report file created: ${TEST_REPORT_FILE}";
    echo ""; echo "~~~ The test coverage report can be found by opening: ${COVERAGE_REPORT_FILE}"

    echo ""
    if [[ ${test_run_exit_code} -eq 0 ]]; then
       echo "SUCCESSFUL: all tests have successfully PASSED."
    else
       echo "FAILURE: one or more tests have FAILED or another reason for failure returned by 'pytest'."
    fi
    echo ""; echo "Exiting with error code '${test_run_exit_code}'."
}

print_start_time
delete_the_old_test_report
delete_the_old_coverage_report_folder_and_create_a_new_one
run_test_runner
print_finish_time

exit ${test_run_exit_code}