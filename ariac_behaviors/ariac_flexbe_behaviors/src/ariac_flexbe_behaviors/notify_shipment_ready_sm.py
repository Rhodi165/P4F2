#!/usr/bin/env python
# -*- coding: utf-8 -*-
###########################################################
#               WARNING: Generated code!                  #
#              **************************                 #
# Manual changes may get lost if file is generated again. #
# Only code inside the [MANUAL] tags will be kept.        #
###########################################################

from flexbe_core import Behavior, Autonomy, OperatableStateMachine, ConcurrencyContainer, PriorityContainer, Logger
from flexbe_states.wait_state import WaitState
from ariac_flexbe_states.notify_shipment_ready_state import NotifyShipmentReadyState
from ariac_flexbe_states.get_agv_status_state import GetAgvStatusState
from ariac_support_flexbe_states.equal_state import EqualState
# Additional imports can be added inside the following tags
# [MANUAL_IMPORT]

# [/MANUAL_IMPORT]


'''
Created on Sat Apr 25 2020
@author: Gerard Harkema
'''
class notify_shipment_readySM(Behavior):
	'''
	Notifies the agv the shipment is ready
This is a part of the ariac_example.
	'''


	def __init__(self):
		super(notify_shipment_readySM, self).__init__()
		self.name = 'notify_shipment_ready'

		# parameters of this behavior

		# references to used behaviors

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		# x:744 y:163, x:229 y:196
		_state_machine = OperatableStateMachine(outcomes=['finished', 'failed'])
		_state_machine.userdata.agv_id = "agv1"
		_state_machine.userdata.shipment_type = 'order_0_shepment_0'
		_state_machine.userdata.inspection_result = ""
		_state_machine.userdata.success = 0
		_state_machine.userdata.agv_state = ""
		_state_machine.userdata.agv_ready_state = "ready_to_deliver"

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]


		with _state_machine:
			# x:200 y:39
			OperatableStateMachine.add('NotifyShipmentReady',
										NotifyShipmentReadyState(),
										transitions={'continue': 'Wait', 'fail': 'failed'},
										autonomy={'continue': Autonomy.Off, 'fail': Autonomy.Off},
										remapping={'agv_id': 'agv_id', 'shipment_type': 'shipment_type', 'success': 'success', 'message': 'message'})

			# x:523 y:46
			OperatableStateMachine.add('GetAgvState',
										GetAgvStatusState(),
										transitions={'continue': 'AgvReady', 'fail': 'failed'},
										autonomy={'continue': Autonomy.Off, 'fail': Autonomy.Off},
										remapping={'agv_id': 'agv_id', 'agv_state': 'agv_state'})

			# x:503 y:161
			OperatableStateMachine.add('AgvReady',
										EqualState(),
										transitions={'true': 'finished', 'false': 'Wait'},
										autonomy={'true': Autonomy.Off, 'false': Autonomy.Off},
										remapping={'value_a': 'agv_state', 'value_b': 'agv_ready_state'})

			# x:408 y:42
			OperatableStateMachine.add('Wait',
										WaitState(wait_time=1),
										transitions={'done': 'GetAgvState'},
										autonomy={'done': Autonomy.Off})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
