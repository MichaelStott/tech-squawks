#!bin/bash

working_dir="${WORKING_DIR//\\//}"
echo $working_dir
if [[ $working_dir == *py ]] 
then
  pip install -r requirements.txt
elif [[ $working_dir == *ts ]] 
then
  npm i
elif [[ $working_dir == *js ]] 
then
  npm i
elif [[ $working_dir == *go ]] 
then
  go mod init
else
  echo "Cannot detect language from directory: " + $working_dir; 
fi
