#!/bin/bash
#Author: Yasen Wang

#====VARIABLE STAGE====
VIRTUAL_PATH='/data/env/bin'
WEB_ROOT='/data/wwwroot/counsellor'
SH_NAME='COUNSELLOR RUNNER'


#====FUNCTION STAGE====
#config virtual env.
function env() {
  if [ -d "$VIRTUAL_PATH" ];then
    cd "$VIRTUAL_PATH" || return
      source activate
  else
    echo "Error:Failed to set virtual Environment."
  fi
}
#start project when physic server is restart.
function start() {
  echo ''
}
#update project when github has changed.
function update() {
  echo "Updating project from Git Server..."
  git pull
}


#====MAIN STAGE====
echo "Working SH file $0"
if [ '-start' == "$1" ];then
  start
elif [ '-update' == "$1" ]; then
  update
fi


