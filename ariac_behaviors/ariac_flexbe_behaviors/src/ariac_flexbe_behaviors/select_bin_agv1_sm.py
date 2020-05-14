#!/usr/bin/env python
# -*- coding: utf-8 -*-
###########################################################
#               WARNING: Generated code!                  #
#              **************************                 #
# Manual changes may get lost if file is generated again. #
# Only code inside the [MANUAL] tags will be kept.        #
###########################################################

from flexbe_core import Behavior, Autonomy, OperatableStateMachine, ConcurrencyContainer, PriorityContainer, Logger
from ariac_flexbe_states.srdf_state_to_moveit_ariac_state import SrdfStateToMoveitAriac
from ariac_support_flexbe_states.equal_state import EqualState
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
		# x:985 y:749, x:1737 y:522
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
		_state_machine.userdata.move_bin6_1 = 'bin1_1PreGrasp'
		_state_machine.userdata.move_group = ''
		_state_machine.userdata.robot_1 = '/ariac/arm1'
		_state_machine.userdata.action_topic = '/move_group'
		_state_machine.userdata.robot_name = ''
		_state_machine.userdata.move_bin5_1 = 'bin2_1PreGrasp'
		_state_machine.userdata.move_bin2_2 = 'bin5_2PreGrasp'
		_state_machine.userdata.move_bin1_2 = 'bin6_2PreGrasp'
		_state_machine.userdata.move_bin4_1 = 'bin3_1PreGrasp'
		_state_machine.userdata.move_bin4_2 = 'bin3_2PreGrasp'
		_state_machine.userdata.robot_2 = '/ariac/arm2'
		_state_machine.userdata.move_home = 'home'
		_state_machine.userdata.move_agv1 = 'tray1PreDrop'

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]


		with _state_machine:
			# x:74 y:59
			OperatableStateMachine.add('MoveR1Home1',
										SrdfStateToMoveitAriac(),
										transitions={'reached': 'MoveR2Home1', 'planning_failed': 'failed', 'control_failed': 'failed', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'move_home', 'move_group': 'move_group', 'move_group_prefix': 'robot_1', 'action_topic': 'action_topic', 'robot_name': 'robot_name', 'config_name_out': 'config_name_out', 'move_group_out': 'move_group_out', 'robot_name_out': 'robot_name_out', 'action_topic_out': 'action_topic_out', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:942 y:27
			OperatableStateMachine.add('Bin_5',
										EqualState(),
										transitions={'true': 'Robot1ToBin5', 'false': 'Bin_6'},
										autonomy={'true': Autonomy.Off, 'false': Autonomy.Off},
										remapping={'value_a': 'bin_location', 'value_b': 'bin_5'})

			# x:1280 y:27
			OperatableStateMachine.add('Bin_6',
										EqualState(),
										transitions={'true': 'Robot1ToBin6', 'false': 'Belt'},
										autonomy={'true': Autonomy.Off, 'false': Autonomy.Off},
										remapping={'value_a': 'bin_location', 'value_b': 'bin_6'})

			# x:1606 y:27
			OperatableStateMachine.add('Belt',
										EqualState(),
										transitions={'true': 'finished', 'false': 'failed'},
										autonomy={'true': Autonomy.Off, 'false': Autonomy.Off},
										remapping={'value_a': 'bin_location', 'value_b': 'belt'})

			# x:604 y:27
			OperatableStateMachine.add('Bin_2',
										EqualState(),
										transitions={'true': 'Robot2ToBin2', 'false': 'Bin_5'},
										autonomy={'true': Autonomy.Off, 'false': Autonomy.Off},
										remapping={'value_a': 'bin_location', 'value_b': 'bin_2'})

			# x:1290 y:109
			OperatableStateMachine.add('Robot1ToBin6',
										SrdfStateToMoveitAriac(),
										transitions={'reached': 'MoveR1Agv1', 'planning_failed': 'failed', 'control_failed': 'failed', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'move_bin6_1', 'move_group': 'move_group', 'move_group_prefix': 'robot_1', 'action_topic': 'action_topic', 'robot_name': 'robot_name', 'config_name_out': 'config_name_out', 'move_group_out': 'move_group_out', 'robot_name_out': 'robot_name_out', 'action_topic_out': 'action_topic_out', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:954 y:116
			OperatableStateMachine.add('Robot1ToBin5',
										SrdfStateToMoveitAriac(),
										transitions={'reached': 'MoveR1Agv1', 'planning_failed': 'failed', 'control_failed': 'failed', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'move_bin5_1', 'move_group': 'move_group', 'move_group_prefix': 'robot_1', 'action_topic': 'action_topic', 'robot_name': 'robot_name', 'config_name_out': 'config_name_out', 'move_group_out': 'move_group_out', 'robot_name_out': 'robot_name_out', 'action_topic_out': 'action_topic_out', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:613 y:111
			OperatableStateMachine.add('Robot2ToBin2',
										SrdfStateToMoveitAriac(),
										transitions={'reached': 'MoveR2Bin4', 'planning_failed': 'failed', 'control_failed': 'failed', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'move_bin2_2', 'move_group': 'move_group', 'move_group_prefix': 'robot_2', 'action_topic': 'action_topic', 'robot_name': 'robot_name', 'config_name_out': 'config_name_out', 'move_group_out': 'move_group_out', 'robot_name_out': 'robot_name_out', 'action_topic_out': 'action_topic_out', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:250 y:109
			OperatableStateMachine.add('Robot2ToBin1',
										SrdfStateToMoveitAriac(),
										transitions={'reached': 'MoveR2Bin4', 'planning_failed': 'failed', 'control_failed': 'failed', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'move_bin1_2', 'move_group': 'move_group', 'move_group_prefix': 'robot_2', 'action_topic': 'action_topic', 'robot_name': 'robot_name', 'config_name_out': 'config_name_out', 'move_group_out': 'move_group_out', 'robot_name_out': 'robot_name_out', 'action_topic_out': 'action_topic_out', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:442 y:203
			OperatableStateMachine.add('MoveR2Bin4',
										SrdfStateToMoveitAriac(),
										transitions={'reached': 'MoveR2Home2', 'planning_failed': 'failed', 'control_failed': 'failed', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'move_bin4_2', 'move_group': 'move_group', 'move_group_prefix': 'robot_2', 'action_topic': 'action_topic', 'robot_name': 'robot_name', 'config_name_out': 'config_name_out', 'move_group_out': 'move_group_out', 'robot_name_out': 'robot_name_out', 'action_topic_out': 'action_topic_out', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:440 y:441
			OperatableStateMachine.add('MoveR1Bin4',
										SrdfStateToMoveitAriac(),
										transitions={'reached': 'MoveR1Agv1', 'planning_failed': 'failed', 'control_failed': 'failed', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'move_bin4_1', 'move_group': 'move_group', 'move_group_prefix': 'robot_1', 'action_topic': 'action_topic', 'robot_name': 'robot_name', 'config_name_out': 'config_name_out', 'move_group_out': 'move_group_out', 'robot_name_out': 'robot_name_out', 'action_topic_out': 'action_topic_out', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:441 y:322
			OperatableStateMachine.add('MoveR2Home2',
										SrdfStateToMoveitAriac(),
										transitions={'reached': 'MoveR1Bin4', 'planning_failed': 'failed', 'control_failed': 'failed', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'move_home', 'move_group': 'move_group', 'move_group_prefix': 'robot_2', 'action_topic': 'action_topic', 'robot_name': 'robot_name', 'config_name_out': 'config_name_out', 'move_group_out': 'move_group_out', 'robot_name_out': 'robot_name_out', 'action_topic_out': 'action_topic_out', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:933 y:506
			OperatableStateMachine.add('MoveR1Agv1',
										SrdfStateToMoveitAriac(),
										transitions={'reached': 'MoveR1Home2', 'planning_failed': 'failed', 'control_failed': 'failed', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'move_agv1', 'move_group': 'move_group', 'move_group_prefix': 'robot_1', 'action_topic': 'action_topic', 'robot_name': 'robot_name', 'config_name_out': 'config_name_out', 'move_group_out': 'move_group_out', 'robot_name_out': 'robot_name_out', 'action_topic_out': 'action_topic_out', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:933 y:627
			OperatableStateMachine.add('MoveR1Home2',
										SrdfStateToMoveitAriac(),
										transitions={'reached': 'finished', 'planning_failed': 'failed', 'control_failed': 'failed', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'move_home', 'move_group': 'move_group', 'move_group_prefix': 'robot_1', 'action_topic': 'action_topic', 'robot_name': 'robot_name', 'config_name_out': 'config_name_out', 'move_group_out': 'move_group_out', 'robot_name_out': 'robot_name_out', 'action_topic_out': 'action_topic_out', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:76 y:198
			OperatableStateMachine.add('MoveR2Home1',
										SrdfStateToMoveitAriac(),
										transitions={'reached': 'Bin_1', 'planning_failed': 'failed', 'control_failed': 'failed', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'move_home', 'move_group': 'move_group', 'move_group_prefix': 'robot_2', 'action_topic': 'action_topic', 'robot_name': 'robot_name', 'config_name_out': 'config_name_out', 'move_group_out': 'move_group_out', 'robot_name_out': 'robot_name_out', 'action_topic_out': 'action_topic_out', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:247 y:25
			OperatableStateMachine.add('Bin_1',
										EqualState(),
										transitions={'true': 'Robot2ToBin1', 'false': 'Bin_2'},
										autonomy={'true': Autonomy.Off, 'false': Autonomy.Off},
										remapping={'value_a': 'bin_location', 'value_b': 'bin_1'})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
