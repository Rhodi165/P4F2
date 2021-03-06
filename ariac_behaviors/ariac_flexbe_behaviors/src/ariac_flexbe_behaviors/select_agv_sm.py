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
from ariac_flexbe_behaviors.select_bin_agv1_sm import select_bin_agv1SM
from ariac_flexbe_behaviors.select_bin_agv2_sm import select_bin_agv2SM
# Additional imports can be added inside the following tags
# [MANUAL_IMPORT]

# [/MANUAL_IMPORT]


'''
Created on Wed May 13 2020
@author: Lein van Sluijs
'''
class SelectagvSM(Behavior):
	'''
	select the right agv
	'''


	def __init__(self):
		super(SelectagvSM, self).__init__()
		self.name = 'Select agv'

		# parameters of this behavior

		# references to used behaviors
		self.add_behavior(select_bin_agv1SM, 'select_bin_agv1')
		self.add_behavior(select_bin_agv2SM, 'select_bin_agv2')

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		# x:636 y:154, x:633 y:106
		_state_machine = OperatableStateMachine(outcomes=['finished', 'failed'], input_keys=['agv_id', 'pose_on_agv', 'bin_location', 'part_type'])
		_state_machine.userdata.agv_id = ''
		_state_machine.userdata.agv_1 = 'agv1'
		_state_machine.userdata.agv_2 = 'agv2'
		_state_machine.userdata.bin_location = ''
		_state_machine.userdata.pose_on_agv = []
		_state_machine.userdata.part_type = ''

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]


		with _state_machine:
			# x:269 y:41
			OperatableStateMachine.add('Agv1',
										EqualState(),
										transitions={'true': 'select_bin_agv1', 'false': 'Agv2'},
										autonomy={'true': Autonomy.Off, 'false': Autonomy.Off},
										remapping={'value_a': 'agv_id', 'value_b': 'agv_1'})

			# x:267 y:141
			OperatableStateMachine.add('select_bin_agv1',
										self.use_behavior(select_bin_agv1SM, 'select_bin_agv1'),
										transitions={'finished': 'finished', 'failed': 'failed'},
										autonomy={'finished': Autonomy.Inherit, 'failed': Autonomy.Inherit},
										remapping={'part_type': 'part_type', 'pose_on_agv': 'pose_on_agv', 'bin_location': 'bin_location'})

			# x:850 y:43
			OperatableStateMachine.add('Agv2',
										EqualState(),
										transitions={'true': 'select_bin_agv2', 'false': 'failed'},
										autonomy={'true': Autonomy.Off, 'false': Autonomy.Off},
										remapping={'value_a': 'agv_id', 'value_b': 'agv_2'})

			# x:845 y:135
			OperatableStateMachine.add('select_bin_agv2',
										self.use_behavior(select_bin_agv2SM, 'select_bin_agv2'),
										transitions={'finished': 'finished', 'failed': 'failed'},
										autonomy={'finished': Autonomy.Inherit, 'failed': Autonomy.Inherit},
										remapping={'bin_location': 'bin_location', 'pose_on_agv': 'pose_on_agv', 'part_type': 'part_type'})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
