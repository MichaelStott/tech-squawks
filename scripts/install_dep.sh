#!bin/bash

working_dir="${WORKING_DIR//\\//}"
echo $working_dir
if [[ $working_dir == *py ]] 
then
  python3 -m venv "$working_dir/env" 
  pip install -r "$working_dir/requirements.txt" 
elif [[ $working_dir == *ts ]] 
then
  npm i --prefix $working_dir
elif [[ $working_dir == *js ]] 
then
  npm i --prefix $working_dir
elif [[ $working_dir == *go ]] 
then
  echo "Go project; Nothing to do."
else
  echo "Cannot detect language from directory: " + $working_dir; 
fi
