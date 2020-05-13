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
from ariac_flexbe_states.message_state import MessageState
# Additional imports can be added inside the following tags
# [MANUAL_IMPORT]

# [/MANUAL_IMPORT]


'''
Created on Wed May 13 2020
@author: Lein van Sluijs
'''
class select_bin_agv1SM(Behavior):
	'''
	select the right bin for planning to agv 1
	'''


	def __init__(self):
		super(select_bin_agv1SM, self).__init__()
		self.name = 'select_bin_agv1'

		# parameters of this behavior

		# references to used behaviors

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		# x:1412 y:366, x:179 y:278
		_state_machine = OperatableStateMachine(outcomes=['finished', 'failed'], input_keys=['part_type', 'pose_on_agv', 'bin_location'])
		_state_machine.userdata.part_type = ''
		_state_machine.userdata.pose_on_agv = []
		_state_machine.userdata.bin_1 = 'bin1'
		_state_machine.userdata.bin_2 = 'bin2'
		_state_machine.userdata.bin_5 = 'bin5'
		_state_machine.userdata.bin_6 = 'bin6'
		_state_machine.userdata.belt = 'belt'
		_state_machine.userdata.tester = 'hey ik kan iets in agv1'
		_state_machine.userdata.bin_location = ''

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]


		with _state_machine:
			# x:435 y:41
			OperatableStateMachine.add('Bin_1',
										EqualState(),
										transitions={'true': 'bin1', 'false': 'Bin_2'},
										autonomy={'true': Autonomy.Off, 'false': Autonomy.Off},
										remapping={'value_a': 'bin_location', 'value_b': 'bin_1'})

			# x:1026 y:45
			OperatableStateMachine.add('Bin_5',
										EqualState(),
										transitions={'true': 'bin1', 'false': 'Bin_6'},
										autonomy={'true': Autonomy.Off, 'false': Autonomy.Off},
										remapping={'value_a': 'bin_location', 'value_b': 'bin_5'})

			# x:1373 y:49
			OperatableStateMachine.add('Bin_6',
										EqualState(),
										transitions={'true': 'bin1', 'false': 'Belt'},
										autonomy={'true': Autonomy.Off, 'false': Autonomy.Off},
										remapping={'value_a': 'bin_location', 'value_b': 'bin_6'})

			# x:1607 y:55
			OperatableStateMachine.add('Belt',
										EqualState(),
										transitions={'true': 'Testjes', 'false': 'Testjes'},
										autonomy={'true': Autonomy.Off, 'false': Autonomy.Off},
										remapping={'value_a': 'bin_location', 'value_b': 'belt'})

			# x:427 y:272
			OperatableStateMachine.add('bin1',
										MessageState(),
										transitions={'continue': 'finished'},
										autonomy={'continue': Autonomy.Off},
										remapping={'message': 'tester'})

			# x:1369 y:271
			OperatableStateMachine.add('Testjes',
										MessageState(),
										transitions={'continue': 'finished'},
										autonomy={'continue': Autonomy.Off},
										remapping={'message': 'bin_location'})

			# x:727 y:42
			OperatableStateMachine.add('Bin_2',
										EqualState(),
										transitions={'true': 'bin1', 'false': 'Bin_5'},
										autonomy={'true': Autonomy.Off, 'false': Autonomy.Off},
										remapping={'value_a': 'bin_location', 'value_b': 'bin_2'})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
