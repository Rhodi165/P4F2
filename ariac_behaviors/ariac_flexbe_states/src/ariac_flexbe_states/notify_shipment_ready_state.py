#!/usr/bin/env python

import sys
import rospy

from flexbe_core import EventState, Logger
from osrf_gear.srv import AGVControl, AGVControlRequest, AGVControlResponse


class NotifyShipmentReadyState(EventState):
	'''
	Notify the shipment is ready for transportation

	<# agv_id 		string 	agv_id: agv1 or agv2 to select the desired agv
	<# shipment_type	string	Id of the order

	#> success		bool	Result of the inspection
	#> message		string

	<= continue 		Given time has passed.
	<= fail			

	'''

	def __init__(self):
		# Declare outcomes, input_keys, and output_keys by calling the super constructor with the corresponding arguments.
		super(NotifyShipmentReadyState, self).__init__(outcomes = ['continue', 'fail'], input_keys = ['agv_id', 'shipment_type'], output_keys = ['success', 'message'])



	def execute(self, userdata):
		# This method is called periodically while the state is active.
		# Main purpose is to check state conditions and trigger a corresponding outcome.
		# If no outcome is returned, the state will stay active.

		# initialize service proxy
		if userdata.agv_id == 'agv1':
			rospy.wait_for_service('/ariac/agv1')
			NotifyShipmentReady = rospy.ServiceProxy('/ariac/agv1', AGVControl)
		else:
			if userdata.destination_id == 'agv2':
				rospy.wait_for_service('/ariac/agv2')
				NotifyShipmentReady = rospy.ServiceProxy('/ariac/agv2', AGVControl)
			else:
				userdata.success = None
				userdata.message = None
				return 'fail'


		request = AGVControlRequest()
		request.shipment_type = userdata.shipment_type
		try:
			srv_result = NotifyShipmentReady(request)
			userdata.success = srv_result.success
			userdata.message = srv_result.message
			return 'continue'

		except Exception as e:
			Logger.logwarn('Could not submet shipment, service call failed')
			rospy.logwarn(str(e))
			userdata.message = None
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
		
