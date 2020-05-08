#!/usr/bin/env python
# -*- coding: utf-8 -*-
###########################################################
#               WARNING: Generated code!                  #
#              **************************                 #
# Manual changes may get lost if file is generated again. #
# Only code inside the [MANUAL] tags will be kept.        #
###########################################################

from flexbe_core import Behavior, Autonomy, OperatableStateMachine, ConcurrencyContainer, PriorityContainer, Logger
from ariac_support_flexbe_states.add_numeric_state import AddNumericState
from ariac_flexbe_states.message_state import MessageState
from ariac_support_flexbe_states.greater_numeric_state import GreaterNumericState
# Additional imports can be added inside the following tags
# [MANUAL_IMPORT]

# [/MANUAL_IMPORT]


'''
Created on Tue Apr 21 2020
@author: Gerard Harkema
'''
class loop_exampleSM(Behavior):
	'''
	Example to test loops
	'''


	def __init__(self):
		super(loop_exampleSM, self).__init__()
		self.name = 'loop_example'

		# parameters of this behavior

		# references to used behaviors

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		# x:11 y:218
		_state_machine = OperatableStateMachine(outcomes=['finished'])
		_state_machine.userdata.number_of_interations = 5
		_state_machine.userdata.iteration = 0
		_state_machine.userdata.one_value = 1
		_state_machine.userdata.zero_value = 0

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]


		with _state_machine:
			# x:134 y:46
			OperatableStateMachine.add('Add',
										AddNumericState(),
										transitions={'done': 'Compare'},
										autonomy={'done': Autonomy.Off},
										remapping={'value_a': 'one_value', 'value_b': 'iteration', 'result': 'iteration'})

			# x:348 y:202
			OperatableStateMachine.add('Message',
										MessageState(),
										transitions={'continue': 'Add'},
										autonomy={'continue': Autonomy.Off},
										remapping={'message': 'iteration'})

			# x:345 y:46
			OperatableStateMachine.add('Compare',
										GreaterNumericState(),
										transitions={'true': 'finished', 'false': 'Message'},
										autonomy={'true': Autonomy.Off, 'false': Autonomy.Off},
										remapping={'value_a': 'iteration', 'value_b': 'number_of_interations'})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
