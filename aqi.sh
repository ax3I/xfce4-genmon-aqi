#!/bin/bash

# xfce4-genmon script to monitor Air Quality Index
# 2023 (ɔ) Ax3I
#
# 0-50 Good (green)
# 50-100 Moderate (yellow)
# 100-150 Unhealty for Sensitive Groups (orange)
# 150-200 Unhealthy (red)
# 200-300 Very Unhealthy (purple)
# 300-500 Hazardous (burgundy)

moderate=50
unhealthy_sens=100
unhealthy=150
very_unhealthy=200
hazardous=300

aqi=$(python3 "$(dirname "$0")"/main.py)

color='palegreen'
level='Good'
if [[ $aqi -gt $hazardous ]]
then
    color='brown'
    level='Hazardous'
elif [[ $aqi -gt $very_unhealthy ]]
then
    color='plum'
    level='Very Unhealthy'
elif [[ $aqi -gt $unhealthy ]]
then
    color='tomato'
    level='Unhealthy'
elif [[ $aqi -gt $unhealthy_sens ]]
then
    color='orange'
    level='Unhealthy for Sensitive Groups'
elif [[ $aqi -gt $moderate ]]
then
    color='yellow2'
    level='Moderate'
fi
aqi="${aqi}"

echo "<txt><span  weight='Light' background="\'$color\' foreground=\'black\'"> $aqi </span></txt>"
echo -e "<tool>AQI: $aqi $level</tool>"
