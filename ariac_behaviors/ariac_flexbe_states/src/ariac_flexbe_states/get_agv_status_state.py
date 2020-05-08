#!/usr/bin/env python

# Software License Agreement (BSD License)
#
# Copyright (c) 2020, Avans Hogeschool
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above
#    copyright notice, this list of conditions and the following
#    disclaimer in the documentation and/or other materials provided
#    with the distribution.
#  * Neither the name of Avans Hogeschool nor the names of its
#    contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
#
# Authors: Gerard Harkema

import rospy

from flexbe_core import EventState, Logger
from std_srvs.srv import Trigger
from osrf_gear.msg import Order, Shipment
from std_msgs.msg import String

class GetAgvStatusState(EventState):
	'''
	Gets the status of the agv: "ready_to_deliver", "preparing_to_deliver", "delevering", "returning"

	<# agv_id 		string 	agv_id: agv1 or agv2 to select the desired agv

	#> agv_state		string status of the selected agv

	<= continue 		Given time has passed.
	<= fail			

	'''

	def __init__(self):
		# Declare outcomes, input_keys, and output_keys by calling the super constructor with the corresponding arguments.
		super(GetAgvStatusState, self).__init__(outcomes = ['continue', 'fail'], input_keys = ['agv_id'], output_keys = ['agv_state'])


	def execute(self, userdata):
		# This method is called periodically while the state is active.
		# Main purpose is to check state conditions and trigger a corresponding outcome.
		# If no outcome is returned, the state will stay active.
		if userdata.agv_id == 'agv1':
			status = rospy.wait_for_message('/ariac/agv1/state', String)
			userdata.agv_state = status.data
			return 'continue'
		else:
			if userdata.destination_id == 'agv2':
				status = rospy.wait_for_message('/ariac/agv2/state', String)
				userdata.agv_status = status.data
				return 'continue'
			else:
				userdata.agv_state = None
				return 'fail'

	def on_enter(self, userdata):
		# This method is called when the state becomes active, i.e. a transition from another state to this one is taken.
		# It is primarily used to start actions which are associated with this state.
		pass # Nothing to do in this example.



	def on_exit(self, userdata):
		# This method is called when an outcome is returned and another state gets active.
		# It can be used to stop possibly running processes started by on_enter.

		pass # Nothing to do in this example.


	def on_start(self):
		# This method is called when the behavior is started.
		# If possible, it is generally better to initialize used resources in the constructor
		# because if anything failed, the behavior would not even be started.

		pass # Nothing to do in this example.


	def on_stop(self):
		# This method is called whenever the behavior stops execution, also if it is cancelled.
		# Use this event to clean up things like claimed resources.

		pass # Nothing to do in this example.
