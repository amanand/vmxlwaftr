#!/usr/bin/env bash
MGMTIP=$1
IDENTITY=$2
CORES=$3

if [ -z "$IDENTITY" ]; then
  echo "Usage: $0 management-ip-address identity.key"
  exit 1
fi

while :
do
  MANAGER=/snabbvmx_manager.pl
  if [ -f /u/snabbvmx_manager.pl ]; then
     cp /u/snabbvmx_manager.pl /tmp/ 2>/dev/null
     MANAGER=/tmp/snabbvmx_manager.pl
  fi
  $MANAGER $MGMTIP $IDENTITY $CORES
  sleep 5
done
