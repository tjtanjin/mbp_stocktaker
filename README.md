<p align="center">
  <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQO28vh9PSjMCOA3BE-uM5vsMcx7fdETR4U_NZMAmiy9_vygVeNkIjU-efMUOS_O_TRxpprW88&usqp=CAc" />
  <h1 align="center">MBP Stocktaker</h1>
</p>

## Table of Contents
* [Introduction](#introduction)
* [Features](#features)
* [Technologies](#technologies)
* [Setup](#setup)
* [Team](#team)
* [Contributing](#contributing)
* [Others](#others)

### Introduction
MBP Stocktaker, short for Macbook Pro Stocktaker was one of the first automation script I wrote when I started coding. Back then, I had the intention to purchase a refurbished macbook but there was no available stock for the specifications that I wanted. Fearing that others would snatch up the loot when restocked, this script was ran every 15 minutes via crontab to check for the availability of the Macbook based on its price and specs. An email would be sent to me once the stock is available so that I can be the first to grab it!

### Features
This is a simple script that checks for my desired refurbished Macbook Pro's availability.

### Technologies
Technologies used by MBP Stocktaker are as below:
##### Done with:

<p align="center">
  <img height="150" width="150" src="https://logos-download.com/wp-content/uploads/2016/10/Python_logo_icon.png"/>
</p>
<p align="center">
Python
</p>

##### Deployed on:
<p align="center">
  <img height="150" width="150" src="https://i.dlpng.com/static/png/404295_thumb.png" />
</p>
<p align="center">
Digital Ocean
</p>


##### Project Repository
```
https://github.com/tjtanjin/mbp_stocktaker
```

### Setup
The following section will guide you through setting up your own MBP Stocktaker!
* First, cd to the directory of where you wish to store the project and clone this repository. An example is provided below:
```
$ cd /home/user/exampleuser/projects/
$ git clone https://github.com/tjtanjin/mbp_stocktaker.git
```
* Following which, you will need to install google chrome with the following commands:
```
$ wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
$ sudo apt install ./google-chrome-stable_current_amd64.deb
```
* Then, install and setup chromedriver with the commands below:
```
$ wget https://chromedriver.storage.googleapis.com/2.41/chromedriver_linux64.zip
$ unzip chromedriver_linux64.zip
$ sudo mv chromedriver /usr/bin/chromedriver
$ sudo chown root:root /usr/bin/chromedriver
$ sudo chmod +x /usr/bin/chromedriver
```
* Finally, to execute the code every 15 minutes, edit your crontab file with the following command:
```
$ crontab -e
```
Within your crontab file, add the following entry:
```
 */15 * * * * usr/bin/python3 /path/to/where/you/store/mbp_script
```
* Note that both your paths above might differ depending on where your python is installed and its current version. Do also make sure you have selenium installed. The code defaults to headless mode so if you would like to see the browser in action, modify the code to change headless mode to true!
* If you wish to host your telegram bot online 24/7, do checkout the guide [here](https://gist.github.com/tjtanjin/ce560069506e3b6f4d70e570120249ed).

### Team
* [Tan Jin](https://github.com/tjtanjin)

### Contributing
If you have code to contribute to the project, open a pull request and describe clearly the changes and what they are intended to do (enhancement, bug fixes etc). Alternatively, you may simply raise bugs or suggestions by opening an issue.

### Others
For any questions regarding the implementation of the project, please drop an email to: cjtanjin@gmail.com.
