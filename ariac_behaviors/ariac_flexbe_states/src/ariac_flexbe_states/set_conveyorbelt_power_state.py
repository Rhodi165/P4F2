#!/usr/bin/env python

import sys
import rospy

from flexbe_core import EventState, Logger
from osrf_gear.srv import ConveyorBeltControl, ConveyorBeltControlRequest, ConveyorBeltControlResponse


class SetConveyorbeltPowerState(EventState):
	'''
	Sets the conveyor belt power

	># power 		float64 	power of the belt rang 0..100

	<= continue 		Given power has passed.
	<= fail			

	'''

	def __init__(self):
		# Declare outcomes, input_keys, and output_keys by calling the super constructor with the corresponding arguments.
		super(SetConveyorbeltPowerState, self).__init__(outcomes = ['continue', 'fail'], input_keys = ['power'])

		# initialize service proxy
		rospy.wait_for_service('/ariac/conveyor/control')
		self.SetConveyorbeltPower = rospy.ServiceProxy('/ariac/conveyor/control', ConveyorBeltControl)


	def execute(self, userdata):
		# This method is called periodically while the state is active.
		# Main purpose is to check state conditions and trigger a corresponding outcome.
		# If no outcome is returned, the state will stay active.
		request = ConveyorBeltControlRequest()
		request.power = userdata.power
		srv_result = self.SetConveyorbeltPower(request)
		if srv_result.success :
			return 'continue'
		return 'fail'


	def on_enter(self, userdata):
		# This method is called when the state becomes active, i.e. a transition from 
		pass # Nothing to do in this example.

	def on_exit(self, userdata):
		# This method is called when an outcome is returned and another state gets active.
		# It can be used to stop possibly running processes started by on_enter.

		pass # Nothing to do in this example.


	def on_start(self):
		# This method is called when the behavior is started.
		# If possible, it is generally better to initialize used resources in the constructor
		# because if anything failed, the behavior would not even be started.

		# In this example, we use this event to set the correct start time.
		pass # Nothing to do in this example.


	def on_stop(self):
		# This method is called whenever the behavior stops execution, also if it is cancelled.
		# Use this event to clean up things like claimed resources.

		pass # Nothing to do in this example.
		
