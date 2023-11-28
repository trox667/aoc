#!/bin/bash

floor=0
position=0
while read -n1 char; do
    if [[ $char == "(" ]]; then
        ((floor++))
    elif [[ $char == ")" ]]; then
        ((floor--))
    fi
    ((position++))
    if [[ $floor == -1 ]]; then
        echo $position
        break
    fi
done < ../inputs/input01
echo $floor
