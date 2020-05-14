#!/usr/bin/env python
# -*- coding: utf-8 -*-
###########################################################
#               WARNING: Generated code!                  #
#              **************************                 #
# Manual changes may get lost if file is generated again. #
# Only code inside the [MANUAL] tags will be kept.        #
###########################################################

from flexbe_core import Behavior, Autonomy, OperatableStateMachine, ConcurrencyContainer, PriorityContainer, Logger
from ariac_support_flexbe_states.equal_state import EqualState
# Additional imports can be added inside the following tags
# [MANUAL_IMPORT]

# [/MANUAL_IMPORT]


'''
Created on Thu May 14 2020
@author: Lein van Sluijs
'''
class select_bin_agv2SM(Behavior):
	'''
	select the right bin for planning to agv 2
	'''


	def __init__(self):
		super(select_bin_agv2SM, self).__init__()
		self.name = 'select_bin_agv2'

		# parameters of this behavior

		# references to used behaviors

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		# x:923 y:747, x:1688 y:241
		_state_machine = OperatableStateMachine(outcomes=['finished', 'failed'], input_keys=['bin_location', 'pose_on_agv', 'part_type'])
		_state_machine.userdata.bin_location = ''
		_state_machine.userdata.pose_on_agv = []
		_state_machine.userdata.part_type = ''
		_state_machine.userdata.bin_1 = 'bin1'
		_state_machine.userdata.bin_2 = 'bin2'
		_state_machine.userdata.bin_5 = 'bin5'
		_state_machine.userdata.bin_6 = 'bin6'
		_state_machine.userdata.belt = 'belt'

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]


		with _state_machine:
			# x:150 y:56
			OperatableStateMachine.add('Bin_1',
										EqualState(),
										transitions={'true': 'finished', 'false': 'Bin_2'},
										autonomy={'true': Autonomy.Off, 'false': Autonomy.Off},
										remapping={'value_a': 'bin_1', 'value_b': 'bin_location'})

			# x:426 y:57
			OperatableStateMachine.add('Bin_2',
										EqualState(),
										transitions={'true': 'finished', 'false': 'Bin_5'},
										autonomy={'true': Autonomy.Off, 'false': Autonomy.Off},
										remapping={'value_a': 'bin_2', 'value_b': 'bin_location'})

			# x:748 y:58
			OperatableStateMachine.add('Bin_5',
										EqualState(),
										transitions={'true': 'finished', 'false': 'Bin_6'},
										autonomy={'true': Autonomy.Off, 'false': Autonomy.Off},
										remapping={'value_a': 'bin_5', 'value_b': 'bin_location'})

			# x:1133 y:57
			OperatableStateMachine.add('Bin_6',
										EqualState(),
										transitions={'true': 'finished', 'false': 'Belt'},
										autonomy={'true': Autonomy.Off, 'false': Autonomy.Off},
										remapping={'value_a': 'bin_6', 'value_b': 'bin_location'})

			# x:1512 y:53
			OperatableStateMachine.add('Belt',
										EqualState(),
										transitions={'true': 'finished', 'false': 'failed'},
										autonomy={'true': Autonomy.Off, 'false': Autonomy.Off},
										remapping={'value_a': 'belt', 'value_b': 'bin_location'})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
