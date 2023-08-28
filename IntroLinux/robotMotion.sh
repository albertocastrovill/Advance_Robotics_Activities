#!/bin/bash

# Robot Position
x=0
y=0

#Robot Orientation
heading="UP"

moveUP(){
    y=$((y+1))
}

moveDOWN(){
    y=$((y-1))
}

moveLEFT(){
    x=$((x-1))
}

moveRIGHT(){
    x=$((x+1))
}

while true; do
    echo "Robot Pose: ($x, $y), Facing: $heading"
    read -p "Enter a movement (w/s/a/d/q to quit): " movement

    case "$movement" in 
        w) moveUP ;;
        s) moveDOWN ;;
        a) moveLEFT ;;
        d) moveRIGHT ;;
        q) echo "Exit Bash"; break ;;
        *) echo "Invalid Key"

    esac

done

