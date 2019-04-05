# SICK Innovation Contest 2019 - TUNI FASTlab Team
#RINNETUTKA

Application developed for the SICK Innovation Contest 2019 at Tamper University, Finaland.

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
Chrome Version 72+
```

### Installing

A step by step procedure to installing the dependencies required for this program

List of modules required for the program to execute is listed in the [requirements.txt](https://github.com/teddy1496/SICK-Innovation-Contest-2019-TUNI-FASTlab-Team/blob/master/Server/requirements.txt) file. 
To install them open a command window and run:
```
pip install -r requirements.txt
```
*If the system asks for admin priveledges run the below code with sudo. Example "sudo pip install numpy".

For Slider bar support on browser we must install Ion range Slider.
To get this we must initially install yarn. Install yarn by clicking [Yarn](https://yarnpkg.com/lang/en/docs/install/#debian-stable) or following instructions on the link below:

```https://yarnpkg.com/lang/en/docs/install/#debian-stable
https://yarnpkg.com/lang/en/docs/install/#debian-stable
```
After installing yarn Install ion-range-slider using the following command:

```
yarn install ion-range-slider
```
*This can also be installed using npm or bower, using same command by replacing yarn with one of the respective packages.

We also need a special numpy library by ros called "ros-numpy" that is being used for the mathematical computations on 
the data recieved from the sensor. To install this package please visit the link below, or click: [ros-numpy](http://wiki.ros.org/ros_numpy)
```
http://wiki.ros.org/ros_numpy
```


## Deployment

Add additional notes about how to deploy this on a live system


## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Billie Thompson** - *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc
