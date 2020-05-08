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
# Additional imports can be added inside the following tags
# [MANUAL_IMPORT]

# [/MANUAL_IMPORT]


'''
Created on Tue Apr 21 2020
@author: Gerard harkema
'''
class numeric_testsSM(Behavior):
	'''
	Test new numeric functions
	'''


	def __init__(self):
		super(numeric_testsSM, self).__init__()
		self.name = 'numeric_tests'

		# parameters of this behavior

		# references to used behaviors

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		# x:30 y:365
		_state_machine = OperatableStateMachine(outcomes=['finished'])
		_state_machine.userdata.GetalA = 10
		_state_machine.userdata.GetalB = 5
		_state_machine.userdata.GetalC = 0

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]


		with _state_machine:
			# x:30 y:40
			OperatableStateMachine.add('Add',
										AddNumericState(),
										transitions={'done': 'Result'},
										autonomy={'done': Autonomy.Off},
										remapping={'value_a': 'GetalA', 'value_b': 'GetalB', 'result': 'GetalC'})

			# x:211 y:41
			OperatableStateMachine.add('Result',
										MessageState(),
										transitions={'continue': 'finished'},
										autonomy={'continue': Autonomy.Off},
										remapping={'message': 'GetalC'})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
