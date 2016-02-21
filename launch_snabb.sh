#!/usr/bin/env bash
INT=$1
CPUS=$2

if [ -z "$CPUS" ]; then
  echo "Usage: $0 xeX cpu"
  exit 1
fi

SLEEP=${INT:2:1}

while :
do
  # check if there is a snabb binary available in the mounted directory.
  # use that one if yes
  SNABB=/usr/local/bin/snabb
  if [ -f /u/snabb ]; then
    cp /u/snabb /tmp/ 2>/dev/null
    SNABB=/tmp/snabb
  fi
  echo "launch snabbvmx for $INT after $SLEEP seconds ..."
  $SNABB gc # removing stale runtime files created by Snabb
  CMD="taskset -c $CPUS $SNABB snabbvmx lwaftr --conf snabbvmx-lwaftr-${INT}.cfg --id $INT --pci `cat pci_$INT` --mac `cat mac_$INT` --sock %s.socket"
  echo $CMD
  sleep $SLEEP
  $CMD
  sleep 4
done