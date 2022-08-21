#!bin/bash

working_dir="${WORKING_DIR//\\//}"
if [[ $working_dir == *py ]] 
then
  pip install -r requirements.txt -t $working_dir
elif [[ $working_dirR == *ts ]] 
then
  npm i --prefix $working_dir
elif [[ $working_dir == *js ]] 
then
  npm i --prefix $working_dir
elif [[ $working_dir == *go ]] 
then
  echo "Nothing to do."
else
  echo "Cannot detect language from directory: " + $working_dir; 
fi
