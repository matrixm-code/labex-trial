 #!/bin/bash

 # Test script to test add2No.sh

 # Function to compare expected and actual output
 cd ~/project
 rs=0
 compare_output() {
	     expected_output=$1
	     actual_output=$2

		 if [[ "$expected_output" == "$actual_output" ]]; then
			 rs=$(($rs+1))
		 else
				 echo "[FAIL] Output is incorrect"
				 echo "Expected output: $expected_output"
				 echo "Actual output: $actual_output"
		fi
}

 # Test Case 1: Addition using method 1 (expr command)
 echo "Test Case 1: Addition using method 1 (expr command)"
 echo -e "2\n2\n2" | bash add2No.sh > output.txt
 expected_output="2+2 = 4"
 actual_output=$(cat output.txt | tail -n 1)
 compare_output "$expected_output" "$actual_output"
 rm output.txt

 # Test Case 2: Addition using method 2 (bc command)
 echo "Test Case 2: Addition using method 2 (bc command)"
 echo -e "2\n2\n2" | bash add2No.sh > output.txt
 expected_output="2+2 = 4"
 actual_output=$(cat output.txt | tail -n 1)
 compare_output "$expected_output" "$actual_output"
 rm output.txt

 # Test Case 3: Addition using method 3 (( )) command)
 echo "Test Case 3: Addition using method 3 (( )) command"
 echo -e "2\n2\n3" | bash add2No.sh > output.txt
 expected_output="2+2 = 4"
 actual_output=$(cat output.txt | tail -n 1)
 compare_output "$expected_output" "$actual_output"
 rm output.txt
								     
if [[ $rs -eq 3 ]];then
	exit 0
else
	exit 1
fi
