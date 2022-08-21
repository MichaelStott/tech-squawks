
if [[ $name == *py ]] 
then
  pip install -r requirements.txt -t $WORKING_DIR
elif [[ $name == *ts ]]  || [[ $name == *js]] 
then
  npm i --prefix $WORKING_DIR
elif [[ $name == *go]] 
then
  echo "Nothing to do."
else
  echo "Cannot detect language from directory: " + $WORKING_DIR; 
fi
