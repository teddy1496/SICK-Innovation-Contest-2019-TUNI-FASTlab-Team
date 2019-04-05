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


## Deployment

Add additional notes about how to deploy this on a live system


 

## Authors

* **Ronal Bejarano** Email id: ronal.bejarano@tuni.fi 
  **Dharmendra Sharma** Email id: dharmendra.sharma@tuni.fi
  **Nicolas Trimborn** Email id: nicolas.trimborn@tuni.fi
  **Ishira Dewundara** Email id: ishira.dewundaraliyanage@tuni.fi
  **Tarun Devalla** Email id: tarun.devalla@tuni.fi

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc
