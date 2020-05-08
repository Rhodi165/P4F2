#!/usr/bin/env python
# -*- coding: utf-8 -*-
###########################################################
#               WARNING: Generated code!                  #
#              **************************                 #
# Manual changes may get lost if file is generated again. #
# Only code inside the [MANUAL] tags will be kept.        #
###########################################################

from flexbe_core import Behavior, Autonomy, OperatableStateMachine, ConcurrencyContainer, PriorityContainer, Logger
from ariac_flexbe_behaviors.transport_part_from_belt_to_bin_state_sm import transport_part_from_belt_to_bin_stateSM
from ariac_flexbe_states.start_assignment_state import StartAssignment
from ariac_flexbe_states.end_assignment_state import EndAssignment
# Additional imports can be added inside the following tags
# [MANUAL_IMPORT]

# [/MANUAL_IMPORT]


'''
Created on Thu Apr 23 2020
@author: Gerard Harkema
'''
class transport_part_from_belt_to_binSM(Behavior):
	'''
	Transports a part from the belt to the disired bin.
	'''


	def __init__(self):
		super(transport_part_from_belt_to_binSM, self).__init__()
		self.name = 'transport_part_from_belt_to_bin'

		# parameters of this behavior

		# references to used behaviors
		self.add_behavior(transport_part_from_belt_to_bin_stateSM, 'transport_part_from_belt_to_bin_state')

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		# x:636 y:50, x:263 y:129
		_state_machine = OperatableStateMachine(outcomes=['finished', 'failed'])
		_state_machine.userdata.arm = 'arm1'

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]


		with _state_machine:
			# x:49 y:39
			OperatableStateMachine.add('StartAssignment',
										StartAssignment(),
										transitions={'continue': 'transport_part_from_belt_to_bin_state'},
										autonomy={'continue': Autonomy.Off})

			# x:472 y:44
			OperatableStateMachine.add('EndAssignment',
										EndAssignment(),
										transitions={'continue': 'finished'},
										autonomy={'continue': Autonomy.Off})

			# x:196 y:40
			OperatableStateMachine.add('transport_part_from_belt_to_bin_state',
										self.use_behavior(transport_part_from_belt_to_bin_stateSM, 'transport_part_from_belt_to_bin_state'),
										transitions={'finished': 'EndAssignment', 'failed': 'failed'},
										autonomy={'finished': Autonomy.Inherit, 'failed': Autonomy.Inherit},
										remapping={'arm': 'arm'})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
