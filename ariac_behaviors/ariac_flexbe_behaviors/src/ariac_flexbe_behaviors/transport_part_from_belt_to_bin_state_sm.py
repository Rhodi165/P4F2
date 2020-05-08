#!/usr/bin/env python
# -*- coding: utf-8 -*-
###########################################################
#               WARNING: Generated code!                  #
#              **************************                 #
# Manual changes may get lost if file is generated again. #
# Only code inside the [MANUAL] tags will be kept.        #
###########################################################

from flexbe_core import Behavior, Autonomy, OperatableStateMachine, ConcurrencyContainer, PriorityContainer, Logger
from ariac_flexbe_states.dummy_state import DummyState
# Additional imports can be added inside the following tags
# [MANUAL_IMPORT]

# [/MANUAL_IMPORT]


'''
Created on Thu Apr 23 2020
@author: Gerard Harkema
'''
class transport_part_from_belt_to_bin_stateSM(Behavior):
	'''
	Transports a part from pelt to a its own bin.
	'''


	def __init__(self):
		super(transport_part_from_belt_to_bin_stateSM, self).__init__()
		self.name = 'transport_part_from_belt_to_bin_state'

		# parameters of this behavior

		# references to used behaviors

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		# x:332 y:44, x:189 y:128
		_state_machine = OperatableStateMachine(outcomes=['finished', 'failed'], input_keys=['arm'])
		_state_machine.userdata.arm = ''

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]


		with _state_machine:
			# x:137 y:39
			OperatableStateMachine.add('Dummy',
										DummyState(),
										transitions={'done': 'finished'},
										autonomy={'done': Autonomy.Off})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
