#!/bin/bash
# ifconfig
# sudo ip link set wlp0s20f0u4u1 down
# sudo iw wlp0s20f0u4u1 set monitor none
# sudo ip link set wlp0s20f0u4u1 up

# Fake probe request
# probequest --fake wlp0s20f0u2 -o $(pwd)/wifiData.csv

# Real probe request
probequest wlp0s20f0u2 -o $(pwd)/wifiData.csv

chown toxsos $(pwd)/wifiData.csv 