#!/bin/bash
#Author: Yasen Wang

#====variable====
VIRTUAL_PATH='/data/env/bin'
WEB_ROOT='/data/wwwroot/counsellor'
SH_NAME='COUNSELLOR RUNNER'
#config virtual env.
function env() {
  if [ -d "$VIRTUAL_PATH" ];then
    cd "$VIRTUAL_PATH" || return
      source activate
  else
    echo 'Error:Failed to set virtual Environment.'
  fi
}

#start project when physic server is restart.
function start() {
  echo ''
}

#updata project when github has changed.
function update() {
   echo ''
}