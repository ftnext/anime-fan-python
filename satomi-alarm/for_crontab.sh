#!/usr/bin/env bash

set -e

workDir=$(cd $(dirname $0); pwd -P)
htmlFile="${workDir}/autoplay.html"

python3 -m webbrowser -t "file://${htmlFile}"
