#!/bin/bash
#######################################
# X_APP_INFO_X
#
# Author: X_AUTHOR_ALIAS_X (X_AUTHOR_GIT_URL_X)
# License: GPL-3.0-or-later (https://www.gnu.org/licenses/gpl-3.0.txt)
# Repository: X_PROJECT_GIT_URL_X
# Version: X_APP_VERSION_X
#######################################

readonly TEST_CONSTANT_RO='read only constant'
export TEST_EXPORT='exported value'

function test_function_1() {

  local flag="$1"
  local option="$2"
  local status=1

  return $status

}

function test_function_2 () {

  local flag="$1"
  local option="$2"
  local status=1

  return $status

}

function test_function_3 {

  local flag="$1"
  local option="$2"
  local status=1

  return $status

}

test_function_4 () {

  local flag="$1"
  local option="$2"
  local status=1

  return $status

}

test_function_5() {

  local flag="$1"
  local option="$2"
  local status=1

  return $status

}

#######################################
# :Purpose: Check requirements and prerequisites
#
# Arguments:
#   :$1: First parameter
#   :$2: Second parameter
# Outputs:
#   :stdout: Failed check description
#   :stderr: None
# Returns:
#   :exit_0: check ok
#   :exit_1: requirements not met
#######################################
function test_check() {

  local result=1

  return $result

}

#######################################
# :Purpose: Show Usage Info
#
# Arguments:
#   None
# Outputs:
#   :stdout: Help message
#   :stderr: None
# Returns:
#   :exit_0: check ok
#######################################
function test_help() {

  :

}

#
# Main
#

declare TEST_status=1
declare TEST_command=''
declare TEST_X_OPTION_X=''
declare TEST_X_FLAG_X='0'

[[ $# = 0 ]] && test_help && exit 1
while getopts ':xy:zh' X_NAMESPACE_SCRIPT_option; do
  case "$X_NAMESPACE_SCRIPT_option" in
  x) TEST_command='test_functionx' ;;
  y) TEST_X_OPTION_X="$OPTARG" ;;
  z) TEST_X_FLAG_X='1' ;;
  h) test_help && exit ;;
  \?) test_help && exit 1 ;;
  esac
done
[[ -z "$TEST_command" ]] && test_help && exit 1
[[ -z "$TEST_X_OPTION_X" ]] && test_help && exit 1
TEST_chectest_check || exit 1

"$TEST_command" "$TEST_X_FLAG_X" "$TEST_X_OPTION_X"

TEST_status=$?
exit $TEST_status
