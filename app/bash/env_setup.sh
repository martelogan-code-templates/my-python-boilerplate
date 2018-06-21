#!/usr/bin/env bash

if [[ -z $LIB_PATH ]]; then
    if [[ -z $FORCE_CONFIRM ]]; then
        read -p "Please enter path to dependencies library (lib folder) : [default = ${WORKING_DIRECTORY}/lib]:" LIB_PATH
    fi
    if [[ $LIB_PATH = "" ]]; then
        LIB_PATH="${WORKING_DIRECTORY}/lib"
    fi
fi

# attempt to load standard_input_helpers library
source $LIB_PATH/bash-standard-input-helpers/standard_input_helpers.sh;

if [[ ! $? = 0 ]]; then
    printf "\n";
    echo "Failed to source dependencies. Please ensure lib path is correct.";
    printf "\n";
    exit 1;
fi

if ! standard_input_helpers.validate_bash_version_above_3; then
    echo "Script requires bash version >= 3"
    exit 1
fi

if [[ -z $CONFIG_PATH ]]; then
    if [[ -z $FORCE_CONFIRM ]]; then
        if [[ -z $DEFAULT_CONFIG_PROMPT ]]; then
            read -p "Please enter path to apropriate config file: [default = ${DEFAULT_CONFIG_PATH}]:" CONFIG_PATH
        else
            read -p "$DEFAULT_CONFIG_PROMPT" CONFIG_PATH
        fi
    fi
    if [[ $CONFIG_PATH = "" ]]; then
        CONFIG_PATH="${DEFAULT_CONFIG_PATH}"
    fi
fi
