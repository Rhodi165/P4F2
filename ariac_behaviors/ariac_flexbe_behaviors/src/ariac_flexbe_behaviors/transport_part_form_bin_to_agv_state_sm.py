#!/usr/bin/env python
# -*- coding: utf-8 -*-
###########################################################
#               WARNING: Generated code!                  #
#              **************************                 #
# Manual changes may get lost if file is generated again. #
# Only code inside the [MANUAL] tags will be kept.        #
###########################################################

from flexbe_core import Behavior, Autonomy, OperatableStateMachine, ConcurrencyContainer, PriorityContainer, Logger
from ariac_flexbe_states.message_state import MessageState
# Additional imports can be added inside the following tags
# [MANUAL_IMPORT]

# [/MANUAL_IMPORT]


'''
Created on Wed Apr 22 2020
@author: Gerard Harkema
'''
class transport_part_form_bin_to_agv_stateSM(Behavior):
	'''
	transports part from it's bin to the selected agv
	'''


	def __init__(self):
		super(transport_part_form_bin_to_agv_stateSM, self).__init__()
		self.name = 'transport_part_form_bin_to_agv_state'

		# parameters of this behavior

		# references to used behaviors

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		# x:502 y:44, x:223 y:140
		_state_machine = OperatableStateMachine(outcomes=['finished', 'failed'], input_keys=['part_type', 'agv_id', 'pose_on_agv'])
		_state_machine.userdata.part_type = ''
		_state_machine.userdata.agv_id = ''
		_state_machine.userdata.pose_on_agv = []

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]


		with _state_machine:
			# x:30 y:40
			OperatableStateMachine.add('AgvIdMessage',
										MessageState(),
										transitions={'continue': 'PartTypeMessage'},
										autonomy={'continue': Autonomy.Off},
										remapping={'message': 'agv_id'})

			# x:305 y:37
			OperatableStateMachine.add('MoseMessage',
										MessageState(),
										transitions={'continue': 'finished'},
										autonomy={'continue': Autonomy.Off},
										remapping={'message': 'pose_on_agv'})

			# x:171 y:37
			OperatableStateMachine.add('PartTypeMessage',
										MessageState(),
										transitions={'continue': 'MoseMessage'},
										autonomy={'continue': Autonomy.Off},
										remapping={'message': 'part_type'})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
