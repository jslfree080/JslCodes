#!/bin/bash

if test "$4" == ""
then
    echo Usage: screenshot.sh x y w h
else
    NAME=$(date +"%Y%m%d-%H%M%S")

    screencapture -R$1,$2,$3,$4 ~/Documents/screenshot/$NAME.png
fi
exit
