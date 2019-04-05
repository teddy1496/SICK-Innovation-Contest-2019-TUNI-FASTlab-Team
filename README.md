# SICK Innovation Contest 2019 - TUNI FASTlab Team
# RINNETUTKA

Application developed for the SICK Innovation Contest 2019 by FASTlab Team at Tamper University, Finland.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

Here is a list of all the required softwares/system requirements needed to get this program up and running.

```
UBUNTU 16.04 LTS
ROS-Kinetic
Python 2.7
Pip
Yarn
Chrome Version 72+ / Firefox Version 65+
```

### Installing

A step by step procedure to installing the dependencies required for this program

List of modules required for the program to execute is listed in the [requirements.txt](https://github.com/teddy1496/SICK-Innovation-Contest-2019-TUNI-FASTlab-Team/blob/master/requirements.txt) file. 
To install them open a command window and run:
```
pip install -r requirements.txt
```
* If the system asks for admin priveledges run the below code with sudo. Example "sudo pip install numpy".

We require the matplotlib version-2.1.1, You can install this by following the link to the [Matplot Lib 2.1.1](https://github.com/teddy1496/SICK-Innovation-Contest-2019-TUNI-FASTlab-Team/blob/master/requirements.txt) installation instructions.
```
https://github.com/teddy1496/SICK-Innovation-Contest-2019-TUNI-FASTlab-Team/blob/master/requirements.txt
```

For Slider bar support on browser we must install Ion range Slider.
To get this we must initially install yarn. Install [yarn](https://yarnpkg.com/lang/en/docs/install/#debian-stable) by following instructions on the link below:

```https://yarnpkg.com/lang/en/docs/install/#debian-stable
https://yarnpkg.com/lang/en/docs/install/#debian-stable
```
After installing yarn Install ion-range-slider using the following command:

```
yarn add ion-rangeslider
```
* This can also be installed using npm or bower, using same command by replacing yarn with one of the respective packages.

We also need a special numpy library by ros called **"ros-numpy"** that is being used for the mathematical computations on 
the data recieved from the sensor. To install this package please visit the link below, or click: [ros-numpy](http://wiki.ros.org/ros_numpy)
```
http://wiki.ros.org/ros_numpy
```

* To set up the sensor and install the required drivers for the sensor to work on Ubuntu and ROS follow the instructions on 
the [SICKAG GIT Repository](https://github.com/SICKAG/sick_scan) for this Sensor.

## Deployment

* The IP Configuration of the sensor can be done by following [ipconfig.md](https://github.com/SICKAG/sick_scan/blob/master/doc/ipconfig/ipconfig.md) on the [SICKAG GIT Repository](https://github.com/SICKAG/sick_scan).


* Launch Transform file
```
roslaunch sensor_transform.launch
```

* To start the scanner with a specific IP address
```
roslaunch sick_scan sick_mrs_6xxx.launch hostname:=<ip-address>
```

* To start the server
```
python server_BE.py
```
The Server is configured to run on **IP:"192.168.1.222" and Port:"5555"**. 
* You can either configure your host address on the laptop to be "192.168.1.222" **OR**
* You can set the host address on your machine and change line 186 on the file [server_BE.py](https://github.com/teddy1496/SICK-Innovation-Contest-2019-TUNI-FASTlab-Team/blob/master/Server/server_BE.py).

After this configuration open your browser and in the search bar type:
```
<server-ip-address>:<port-number>
``` 
You will have an interface where you can select the area to visualize by selecting the points on the point-cloud using the sliding bars.
The Web Interface has 2 different pages, both pages provides you with the Slope Percentage, Smoothness Index and Weather Forecast.
	* The First Page Provides you with an Image of Slope Surface characteristics.
	* The second page gives a plot defining the Surface Disturbances.
	

## Authors

* **Ronal Bejarano** Email id: ronal.bejarano@tuni.fi 
* **Dharmendra Sharma** Email id: dharmendra.sharma@tuni.fi
* **Nicolas Trimborn** Email id: nicolas.trimborn@tuni.fi
* **Ishira Dewundara** Email id: ishira.dewundaraliyanage@tuni.fi
* **Tarun Devalla** Email id: tarun.devalla@tuni.fi

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc
