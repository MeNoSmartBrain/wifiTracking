# wifiTracking

This project is part of the *Secure Mobile Systems* course at TU Darmstadt from Prof. Dr.-Ing. Matthias Hollick. 

This project tries to show that a lot of private and sensitive information can be won by collecting and analyzing the WiFi probe requests. In combination with publicly-available databases like wigle.net, it is possible to guess the location of where a person lives, works or spends a lot of time.

This project and the documentation is written for strict academical use. The author does not endorse illegal activities like tracking, stacking, or doxing and only permits use of this project for educational purposes, research and demonstration.

## Contents of this project
The main part of this project is written down in a Jupyter Notebook (wifiTracking.ipynb). It contains the majority of the code and the documentation. 

The code can be split into four parts:

### Data collection
The first step is to collect probe requests. For this we need a WiFi adapter that supports monitor mode and the python module "probequest". 
This tool must run with root privileges and can be executed with the probequest.sh script. It stores the collected data in a file called "wifiData.csv".
The data is collected as long as the script is run. Terminate the script with CTRL+C.

### Data structuring
The data is read from the "wifiData.csv" file. The data is structured so the individual MAC addresses are identified. To the MAC addresses the corresponding SSIDs are stored with the individual devices have omitted.

### Data lookup
Using the wigle API for every MAC each SSID is looked up and the corresponding data, like the location, is stored. Since there might be multiple known locations for a single SSID in the wigle database, they are all stored in a list.

The output might look like this:
```
MAC1:
    SSID1:
        Location1
        Location2
    SSID2:
        Location1
MAC2:
    SSID1:
        Location1
```

### Data visualization
The data is visualized using the folium module. With folium the data is displayed on a map using HTML. 
Here each possible location for a SSID is displayed with a semi-transparent marker on the map. All the markers for a single MAC address are given the same color so that it can be easily determined which MAC address is responsible for which marker. 

## Documentation
The documentation is written primarily in the Jupyter Notebook and in the paragraphs above. The code is commented and should be self-explanatory.

## Mitigation
To mitigate the risk of being tracked via WiFi probe requests, we first have to understand what they are.

Devices use probe requests to find WiFi networks known to them. The devices have a preferred network list (PNL) in which all the networks are saved, to which the device has been connected to in the past. With the probe requests the devices try to find these networks known to them. Therefore probe request are to client side equivalent to the beacon frames sent by access points.

By sending the probe requests, the devices reveal their individual PNL, tied to their MAC address, to silent listeners.

### Information contained in probe requests
The following information is simplified to the relevant information and taken from the [IEEE 802.11-2016](https://ieeexplore.ieee.org/document/7786995) standard.
A probe request is a management frame. The management frame is structured as follows (page 692):
|Frame Control|Duration|Destination Address|**Source Address**|BSSID              |SC |Frame Body|FCS|
|-------------|--------|-------------------|------------------|-------------------|---|----------|---|
|             |        | ff:ff:ff:ff:ff:ff | Identifier       | ff:ff:ff:ff:ff:ff |   | see below|   |

In the frame body the following information is contained (page 706-707):
| **SSID**                                           | Supported Rates | HT Capabilities | VHT Capabilities |
|----------------------------------------------------|-----------------|-----------------|------------------|
| The SSID of the network the device is looking for  |                 |                 |                  |

We can see that the management frame with the probe request contains the SSID of the network the device is looking for and the MAC address of the omitting device. 
This is enough information to track a device.

For further information I can recommend the paper "[YOUR MOBILE PHONE IS A TRAITOR! – RAISING AWARENESS ON UBIQUITOUS PRIVACY ISSUES WITH SASQUATCH](https://brambonne.com/docs/bonne14sasquatch.pdf)" by Bram Bonné, Peter Quax and Wim Lamotte in 2014.

### What can be done?
The easiest way to mitigate the risk of being tracked via WiFi probe requests is to disable probe requests. They are not needed to establish a connection to an access point by responding to beacon frames. However this might lead to delays in connecting to a network, since a beacon frame has to be received first.

This is often not directly configurable on the device itself, but many operating systems give the user the choice of "auto reconnect" or "connect to known networks". If this option is disabled, the device will not try to connect to known networks automatically. This is general advice, especially for public networks, since it also prevents attacks like Evil Twin APs.

Additionally MAC address randomization can be used to mitigate the use of a unique identifier. This feature was implemented in [Android 10](https://source.android.com/docs/core/connect/wifi-mac-randomization) and for [iOS](https://support.apple.com/guide/security/wi-fi-privacy-secb9cb3140c/web) on iPhones 5 or later.

This feature is only obfuscation and device identification is still possible. For example an attacker could measure the signal strength of the probe requests or use an antenna with limited range. Additionally, if the attacker measure for a long enough time and the target device is not moving while other device do, the corresponding SSID can be guessed since the would reoccur. 

#### WPA3
WPA3 introduces protected management frames (PMF). This means that attacks like "deauth attacks" are not possible. Since there is not active connecting to a network, the probe requests cannot be protected by PMF. But according to the [WPA3 specification](https://www.wi-fi.org/download.php?file=/sites/default/files/private/WPA3%20Specification%20v3.1.pdf) MAC address randomization is introduced.

## Installation
For the project to run, you will need to be able to run Jupyter Notebooks. I have used the Jupyter Notebook extension for Visual Studio Code.

### Probequest
To install probequest, you will need to install the following dependencies:
```
pip install probequest
```
Proberquest gives the option to generate artificial probe requests. This may be used to test the project. Furthermore this artificial data cannot be correlated to individuals and therefore is not a privacy concern.
To switch between real and artificial data, you can edit the probequest.sh script accordingly.

### requirements.txt
The requirements.txt file should contain all the python modules that are needed for this project. They can be installed with the following command:
```
pip install -r requirements.txt
```

### env.py
In the file "env.py" the access credentials for the wigle API are stored. The file is not included in the repository. The file env.py.sample can be renamed to env.py and the credentials can be added there. The file env.py is ignored by git (part of the .gitignore) and will not be uploaded to the repository.

### Further notes

#### demoMaps folder
The demoMaps folder contains the generated maps and screenshots from artificial probe requests. Check them out to see what the data visualization looks like.

There are code snippets that are inspired by ChatGPT. The unaltered code from ChatGPT can be found in the file "chatGPT.md". Code snippets taken or inspired by ChatGPT are marked in the Jupyter Notebook. These code snippets are not my own creation and should not be considered for grading purposes. 
I have used these code snippets to enhance the visualization of the data. They are not needed for the core functionality of the project.

In the .test.py file you can find code snippets. There are intended to be used to use the clustering capabilities of folium. However, they are not used in the final implementation. I may implement them in a future version of this project, but the code mainly consists of writing JavaScript, CSS and HTML. Furthermore it doesn't directly influence the stated goal of this project. Since my time is limited, I decided to not implement it in the current version.

Therefore this file can be ignored for the grading process.