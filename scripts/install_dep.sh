#!bin/bash

if [[ $WORKING_DIR == *py ]] 
then
  pip install -r requirements.txt -t $WORKING_DIR
elif [[ $WORKING_DIR == *ts ]] 
then
  npm i --prefix $WORKING_DIR
elif [[ $WORKING_DIR == *js ]] 
then
  npm i --prefix $WORKING_DIR
elif [[ $WORKING_DIR == *go ]] 
then
  echo "Nothing to do."
else
  echo "Cannot detect language from directory: " + $WORKING_DIR; 
fi
