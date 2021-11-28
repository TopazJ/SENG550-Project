#!/bin/bash

if [ "$#" -ne 4 ]; then
  echo "Requires year, month, start day, end day"
fi
YEAR=$1
MONTH=$2
DAY=$3
END_DAY=$4
until [ ${DAY} -gt ${END_DAY} ]
do
  if [ ${DAY} -lt 10 ]; then
    if [ ${MONTH} -lt 10 ]; then
      DATE="${YEAR}-0${MONTH}-0${DAY}"
    else
      DATE="${YEAR}-${MONTH}-0${DAY}"
    fi  
  else
    if [ ${MONTH} -lt 10 ]; then
      DATE="${YEAR}-0${MONTH}-${DAY}"
    else
      DATE="${YEAR}-${MONTH}-${DAY}"
    fi  
  fi  
  FILENAME="headlines_${DATE}.json"
  echo $FILENAME
  START_DATE_TIME="${DATE}T00:00:00Z"
  END_DATE_TIME="${DATE}T23:59:59Z"
  echo $START_DATE_TIME
  echo $END_DATE_TIME
  URL="https://gnews.io/api/v4/top-headlines?token=1fa9c832e17e14aa31e82918044dada5&lang=en&from=${START_DATE_TIME}&to=${END_DATE_TIME}"
  echo $URL

  CMD=$(curl ${URL})
  RUNANDSAVE=$(echo $CMD > $FILENAME)
  echo $RUNANDSAVE                                                                                                                                                                                                 
  let DAY++
  # courtesy
  sleep 1
done