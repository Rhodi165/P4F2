#!/usr/bin/env python
# -*- coding: utf-8 -*-
###########################################################
#               WARNING: Generated code!                  #
#              **************************                 #
# Manual changes may get lost if file is generated again. #
# Only code inside the [MANUAL] tags will be kept.        #
###########################################################

from flexbe_core import Behavior, Autonomy, OperatableStateMachine, ConcurrencyContainer, PriorityContainer, Logger
from ariac_flexbe_states.start_assignment_state import StartAssignment
from ariac_flexbe_states.end_assignment_state import EndAssignment
from flexbe_states.wait_state import WaitState
from ariac_flexbe_states.submit_shipment_state import SubmitShipmentState
# Additional imports can be added inside the following tags
# [MANUAL_IMPORT]

# [/MANUAL_IMPORT]


'''
Created on Sat Apr 25 2020
@author: Gerard Harkema
'''
class submit_shipment_exampleSM(Behavior):
	'''
	Example of submitting a shipment
	'''


	def __init__(self):
		super(submit_shipment_exampleSM, self).__init__()
		self.name = 'submit_shipment_example'

		# parameters of this behavior

		# references to used behaviors

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		# x:599 y:55, x:321 y:144
		_state_machine = OperatableStateMachine(outcomes=['finished', 'failed'])
		_state_machine.userdata.agv_id = 'agv1'
		_state_machine.userdata.shipment_type = 'order_0_shipment_0'

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]


		with _state_machine:
			# x:30 y:40
			OperatableStateMachine.add('StartAssignment',
										StartAssignment(),
										transitions={'continue': 'SubmitShipment'},
										autonomy={'continue': Autonomy.Off})

			# x:443 y:42
			OperatableStateMachine.add('EndAssignment',
										EndAssignment(),
										transitions={'continue': 'finished'},
										autonomy={'continue': Autonomy.Off})

			# x:322 y:42
			OperatableStateMachine.add('Wait',
										WaitState(wait_time=30),
										transitions={'done': 'EndAssignment'},
										autonomy={'done': Autonomy.Off})

			# x:167 y:42
			OperatableStateMachine.add('SubmitShipment',
										SubmitShipmentState(),
										transitions={'continue': 'Wait', 'fail': 'failed'},
										autonomy={'continue': Autonomy.Off, 'fail': Autonomy.Off},
										remapping={'agv_id': 'agv_id', 'shipment_type': 'shipment_type', 'inspection_result': 'inspection_result'})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
