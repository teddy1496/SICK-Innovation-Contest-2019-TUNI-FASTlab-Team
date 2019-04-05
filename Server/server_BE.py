#******************************
#           RINNETUTKA
#   TAMPERE UNIVERSITY - FASTLAB
#   SICK INNOVATION COMPETITION 2019
#            BACKEND
#******************************

#******************************
#Libraries
#******************************

from flask import Flask, render_template, request
import json
from Analysis_Sick import slopecalc
from Analysis_Sick import smoothness
from Analysis_Sick import surface_plot
from Analysis_Sick import skiPathComp
import rospy
from sensor_msgs.msg import PointCloud2, PointField
from pylab import *
import ros_numpy
import thread
#from Analysis import test_points3d

# Declare global variables
global umin
global umax
global vmin
global vmax
global ideal
global ideal_flag

# Initialize variables
umin = 0
umax = 920
vmin = 0
vmax = 24
ideal_flag = True

#******************************
#Back End for Web Interface
#******************************
app = Flask(__name__)


@app.route('/<string:page_name>/')
def static_page(page_name):
    return render_template('%s.html' % page_name)


@app.route('/')
def home_page():
    return render_template('test.html')


@app.route('/slope_val', methods=['GET'])
def send_slope_val():
    global slope_val
    # print("sending slope val: {}".format(slope_val))
    slope_val = {"Slope": slope_val}
    slopey = json.dumps(slope_val)
    return slopey


@app.route('/smoothness_val', methods=['GET'])
def send_smoothness_val():
    global smoothness_val
    # print("sending smoothness: {}".format(smoothness_val))
    smoothness_val = {"Smoothness":smoothness_val}
    bumpy = json.dumps(smoothness_val)
    return bumpy


@app.route('/range_layers', methods=['GET'])
def get_range_layer():
    global layers_to
    global layers_from
    global vmin
    global vmax
    global ideal_flag
    ideal_flag = True
    layers_from = request.args.get('layers-from')
    layers_to = request.args.get('layers-to')
    vmin = int(layers_from)
    vmax = int(layers_to)
    # layers_selected = json.dumps(layers)
    # print("my layer vals are: {} {}".format(layers_from,layers_to))
    return "ok"


@app.route('/range_points', methods=['GET'])
def get_range_point():
    global points_to
    global points_from
    global umin
    global umax
    global ideal_flag
    ideal_flag = True
    points_from = request.args.get('points-from')
    points_to = request.args.get('points-to')
    umin = int(points_from)
    umax = int(points_to)
    # print("my point vals are: {} {}".format(points_from,points_to))
    return "ok"


#******************************
#ROS and Data Analytics
#******************************

def subscribePointCloud2FromSick():
    rospy.init_node('sick_mrs_6xxx', anonymous=True)
    msg= rospy.Subscriber('/cloud', PointCloud2, processPointCloud2)
    thread.start_new_thread(flask_Thread, ())
    rospy.spin()


def processPointCloud2(msg):
    # Define common variables with frontend
    global slope_val
    global smoothness_val
    global umin
    global umax
    global vmin
    global vmax
    global xvals
    global ideal_flag
    global ideal
    # Convert PointCloud2 to np.Array
    cld = ros_numpy.numpify(msg, squeeze=False)

    # Create a new cloud with High Intensity (HI) points - Ignore empty areas
    cldHI = cld[cld['intensity'] > 64]
    xHI = cldHI['x'].ravel()
    yHI = cldHI['z'].ravel()
    zHI = -cldHI['y'].ravel()


    # Extract section selected on frontend by sliders and transform
    xvals = cld[vmin:vmax, umin:umax]['x']
    yvals = cld[vmin:vmax, umin:umax]['z']
    zvals = cld[vmin:vmax, umin:umax]['y']
    intsvals = cld[vmin:vmax, umin:umax]['intensity']

    xvals1= xvals[intsvals>64]
    yvals1= yvals[intsvals>64]
    zvals1= -zvals[intsvals>64]

    if ideal_flag:
        ideal = xvals
        ideal_flag = False

    # Ravel section for ploting
    xrav = xvals1.ravel()
    yrav = yvals1.ravel()
    zrav = zvals1.ravel()

    # Indicate sensor position for height correction
    sensorpos = np.array([0, 0, 0])

    # Calculate slope of extracted section
    slope_val = slopecalc(xvals, yvals, sensorpos)

    # Calculate smoothness of extracted section
    smoothness_val = smoothness(yvals)

    # String??
    smoothness_val = str(smoothness_val)

    # Generate frontend images of whole slope  and extracted section
    surface_plot(xHI, yHI, zHI, xrav, yrav, zrav)


    skiPathComp(xvals, ideal)


#******************************
#Initialization
#Main thread: ROS
#Second thread: Flask server
#******************************


def flask_Thread():

    app.run("192.168.1.222", port=5555)


if __name__ == '__main__':

    subscribePointCloud2FromSick()
