#!/bin/bash


runtest () {
  # $1: input
  # $2: testname
  INPUT_FILE=$1
  TEST_NAME=$2
  OUTPUT_FILE="outputs/${TEST_NAME}_output.txt"
  if [ -f "$OUTPUT_FILE" ]; then
    echo "File $OUTPUT_FILE exists."
  else
    touch "$OUTPUT_FILE"
    echo "File $OUTPUT_FILE created."
  fi
  # run test and check time
  start=$(date +%s.%N)
  python ../cs412_longestpath_exact.py < "inputs/${INPUT_FILE}" > "$OUTPUT_FILE"
  end=$(date +%s.%N)
  elapsed=$(echo "$end - $start" | bc)

  dos2unix "$OUTPUT_FILE" "expected/${TEST_NAME}_expected.txt" >/dev/null 2>&1
  if diff -q "$OUTPUT_FILE" "expected/${TEST_NAME}_expected.txt" >/dev/null; then
    echo "${TEST_NAME} PASS"
  else
    echo "${TEST_NAME} FAIL"
    echo "Differences:"
    diff "$OUTPUT_FILE" "expected/${TEST_NAME}_expected.txt"
  fi
  echo "$2 took ${elapsed} seconds to run"
}

# some test cases were made by chatGPT

runtest input1.txt test1
runtest singlepath.txt singlepath
runtest cycle.txt cycle
runtest medium.txt medium
# runtest large_weighted_graph1.txt large1
# runtest large_weighted_graph2.txt large2
# runtest large_weighted_graph3.txt large3
# runtest large_weighted_graph4.txt large4
# runtest large_weighted_graph5.txt large5
# runtest large_weighted_graph6.txt large6
# runtest large_weighted_graph.txt large takes like 40 minutes
runtest bigtest.txt bigtest