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
from ariac_flexbe_behaviors.waitstate_sm import WaitstateSM
# Additional imports can be added inside the following tags
# [MANUAL_IMPORT]

# [/MANUAL_IMPORT]


'''
Created on Thu May 14 2020
@author: Lein en TImon
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
		self.add_behavior(WaitstateSM, 'Waitstate')
		self.add_behavior(WaitstateSM, 'Waitstate_2')
		self.add_behavior(WaitstateSM, 'Waitstate_3')
		self.add_behavior(WaitstateSM, 'Waitstate_4')
		self.add_behavior(WaitstateSM, 'Waitstate_5')
		self.add_behavior(WaitstateSM, 'Waitstate_6')
		self.add_behavior(WaitstateSM, 'Waitstate_7')
		self.add_behavior(WaitstateSM, 'Waitstate_8')
		self.add_behavior(WaitstateSM, 'Waitstate_9')
		self.add_behavior(WaitstateSM, 'Waitstate_10')
		self.add_behavior(WaitstateSM, 'Waitstate_11')

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		# x:1345 y:854, x:913 y:17
		_state_machine = OperatableStateMachine(outcomes=['finished', 'failed'], input_keys=['bin_location', 'pose_on_agv', 'part_type'])
		_state_machine.userdata.bin_location = ''
		_state_machine.userdata.pose_on_agv = []
		_state_machine.userdata.part_type = ''
		_state_machine.userdata.bin_1 = 'bin1'
		_state_machine.userdata.bin_2 = 'bin2'
		_state_machine.userdata.bin_5 = 'bin5'
		_state_machine.userdata.bin_6 = 'bin6'
		_state_machine.userdata.belt = 'belt'
		_state_machine.userdata.move_group = ''
		_state_machine.userdata.action_topic = '/move_group'
		_state_machine.userdata.move_bin5_1 = 'bin2_1PreGrasp'
		_state_machine.userdata.move_bin4_1 = 'bin3_1PreGrasp'
		_state_machine.userdata.move_bin4_2 = 'bin3_2PreGrasp'
		_state_machine.userdata.move_bin2_2 = 'bin5_2PreGrasp'
		_state_machine.userdata.move_bin1_2 = 'bin6_2PreGrasp'
		_state_machine.userdata.move_bin6_1 = 'bin1_1PreGrasp'
		_state_machine.userdata.robot_1 = '/ariac/arm1'
		_state_machine.userdata.robot_2 = '/ariac/arm2'
		_state_machine.userdata.move_home = 'home'
		_state_machine.userdata.move_agv2 = 'tray2PreDrop'
		_state_machine.userdata.robot_name = ''

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]


		with _state_machine:
			# x:83 y:40
			OperatableStateMachine.add('MoveR1Home',
										SrdfStateToMoveitAriac(),
										transitions={'reached': 'MoveR2home', 'planning_failed': 'Waitstate', 'control_failed': 'Waitstate', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'move_home', 'move_group': 'move_group', 'move_group_prefix': 'robot_1', 'action_topic': 'action_topic', 'robot_name': 'robot_name', 'config_name_out': 'config_name_out', 'move_group_out': 'move_group_out', 'robot_name_out': 'robot_name_out', 'action_topic_out': 'action_topic_out', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:744 y:79
			OperatableStateMachine.add('Bin_2',
										EqualState(),
										transitions={'true': 'Robot2toBin2', 'false': 'Bin_5'},
										autonomy={'true': Autonomy.Off, 'false': Autonomy.Off},
										remapping={'value_a': 'bin_2', 'value_b': 'bin_location'})

			# x:1021 y:83
			OperatableStateMachine.add('Bin_5',
										EqualState(),
										transitions={'true': 'Robot1toBin5', 'false': 'Bin_6'},
										autonomy={'true': Autonomy.Off, 'false': Autonomy.Off},
										remapping={'value_a': 'bin_5', 'value_b': 'bin_location'})

			# x:1285 y:84
			OperatableStateMachine.add('Bin_6',
										EqualState(),
										transitions={'true': 'Robot1toBin6', 'false': 'Belt'},
										autonomy={'true': Autonomy.Off, 'false': Autonomy.Off},
										remapping={'value_a': 'bin_6', 'value_b': 'bin_location'})

			# x:1554 y:84
			OperatableStateMachine.add('Belt',
										EqualState(),
										transitions={'true': 'finished', 'false': 'failed'},
										autonomy={'true': Autonomy.Off, 'false': Autonomy.Off},
										remapping={'value_a': 'belt', 'value_b': 'bin_location'})

			# x:303 y:39
			OperatableStateMachine.add('MoveR2home',
										SrdfStateToMoveitAriac(),
										transitions={'reached': 'Bin_1', 'planning_failed': 'Waitstate_2', 'control_failed': 'Waitstate_2', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'move_home', 'move_group': 'move_group', 'move_group_prefix': 'robot_2', 'action_topic': 'action_topic', 'robot_name': 'robot_name', 'config_name_out': 'config_name_out', 'move_group_out': 'move_group_out', 'robot_name_out': 'robot_name_out', 'action_topic_out': 'action_topic_out', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:516 y:168
			OperatableStateMachine.add('Robot2toBin1',
										SrdfStateToMoveitAriac(),
										transitions={'reached': 'MoveR2toAgv2', 'planning_failed': 'Waitstate_3', 'control_failed': 'Waitstate_3', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'move_bin1_2', 'move_group': 'move_group', 'move_group_prefix': 'robot_2', 'action_topic': 'action_topic', 'robot_name': 'robot_name', 'config_name_out': 'config_name_out', 'move_group_out': 'move_group_out', 'robot_name_out': 'robot_name_out', 'action_topic_out': 'action_topic_out', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:754 y:171
			OperatableStateMachine.add('Robot2toBin2',
										SrdfStateToMoveitAriac(),
										transitions={'reached': 'MoveR2toAgv2', 'planning_failed': 'Waitstate_4', 'control_failed': 'Waitstate_4', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'move_bin2_2', 'move_group': 'move_group', 'move_group_prefix': 'robot_2', 'action_topic': 'action_topic', 'robot_name': 'robot_name', 'config_name_out': 'config_name_out', 'move_group_out': 'move_group_out', 'robot_name_out': 'robot_name_out', 'action_topic_out': 'action_topic_out', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:1040 y:173
			OperatableStateMachine.add('Robot1toBin5',
										SrdfStateToMoveitAriac(),
										transitions={'reached': 'MoveR1toBin4', 'planning_failed': 'Waitstate_10', 'control_failed': 'Waitstate_10', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'move_bin5_1', 'move_group': 'move_group', 'move_group_prefix': 'robot_1', 'action_topic': 'action_topic', 'robot_name': 'robot_name', 'config_name_out': 'config_name_out', 'move_group_out': 'move_group_out', 'robot_name_out': 'robot_name_out', 'action_topic_out': 'action_topic_out', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:1295 y:174
			OperatableStateMachine.add('Robot1toBin6',
										SrdfStateToMoveitAriac(),
										transitions={'reached': 'MoveR1toBin4', 'planning_failed': 'Waitstate_11', 'control_failed': 'Waitstate_11', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'move_bin6_1', 'move_group': 'move_group', 'move_group_prefix': 'robot_1', 'action_topic': 'action_topic', 'robot_name': 'robot_name', 'config_name_out': 'config_name_out', 'move_group_out': 'move_group_out', 'robot_name_out': 'robot_name_out', 'action_topic_out': 'action_topic_out', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:1167 y:376
			OperatableStateMachine.add('MoveR1toBin4',
										SrdfStateToMoveitAriac(),
										transitions={'reached': 'MoveR1toHome2', 'planning_failed': 'Waitstate_9', 'control_failed': 'Waitstate_9', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'move_bin4_1', 'move_group': 'move_group', 'move_group_prefix': 'robot_1', 'action_topic': 'action_topic', 'robot_name': 'robot_name', 'config_name_out': 'config_name_out', 'move_group_out': 'move_group_out', 'robot_name_out': 'robot_name_out', 'action_topic_out': 'action_topic_out', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:1168 y:558
			OperatableStateMachine.add('MoveR1toHome2',
										SrdfStateToMoveitAriac(),
										transitions={'reached': 'MoveR2toBin4', 'planning_failed': 'Waitstate_8', 'control_failed': 'Waitstate_8', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'move_home', 'move_group': 'move_group', 'move_group_prefix': 'robot_1', 'action_topic': 'action_topic', 'robot_name': 'robot_name', 'config_name_out': 'config_name_out', 'move_group_out': 'move_group_out', 'robot_name_out': 'robot_name_out', 'action_topic_out': 'action_topic_out', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:1169 y:637
			OperatableStateMachine.add('MoveR2toBin4',
										SrdfStateToMoveitAriac(),
										transitions={'reached': 'MoveR2toAgv2', 'planning_failed': 'Waitstate_7', 'control_failed': 'Waitstate_7', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'move_bin4_2', 'move_group': 'move_group', 'move_group_prefix': 'robot_2', 'action_topic': 'action_topic', 'robot_name': 'robot_name', 'config_name_out': 'config_name_out', 'move_group_out': 'move_group_out', 'robot_name_out': 'robot_name_out', 'action_topic_out': 'action_topic_out', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:701 y:683
			OperatableStateMachine.add('MoveR2toAgv2',
										SrdfStateToMoveitAriac(),
										transitions={'reached': 'MoveR2toHome2', 'planning_failed': 'Waitstate_5', 'control_failed': 'Waitstate_5', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'move_agv2', 'move_group': 'move_group', 'move_group_prefix': 'robot_2', 'action_topic': 'action_topic', 'robot_name': 'robot_name', 'config_name_out': 'config_name_out', 'move_group_out': 'move_group_out', 'robot_name_out': 'robot_name_out', 'action_topic_out': 'action_topic_out', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:699 y:780
			OperatableStateMachine.add('MoveR2toHome2',
										SrdfStateToMoveitAriac(),
										transitions={'reached': 'finished', 'planning_failed': 'Waitstate_6', 'control_failed': 'Waitstate_6', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'move_home', 'move_group': 'move_group', 'move_group_prefix': 'robot_2', 'action_topic': 'action_topic', 'robot_name': 'robot_name', 'config_name_out': 'config_name_out', 'move_group_out': 'move_group_out', 'robot_name_out': 'robot_name_out', 'action_topic_out': 'action_topic_out', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:13 y:140
			OperatableStateMachine.add('Waitstate',
										self.use_behavior(WaitstateSM, 'Waitstate'),
										transitions={'Waited': 'MoveR1Home'},
										autonomy={'Waited': Autonomy.Inherit})

			# x:197 y:155
			OperatableStateMachine.add('Waitstate_2',
										self.use_behavior(WaitstateSM, 'Waitstate_2'),
										transitions={'Waited': 'MoveR2home'},
										autonomy={'Waited': Autonomy.Inherit})

			# x:330 y:252
			OperatableStateMachine.add('Waitstate_3',
										self.use_behavior(WaitstateSM, 'Waitstate_3'),
										transitions={'Waited': 'Robot2toBin1'},
										autonomy={'Waited': Autonomy.Inherit})

			# x:889 y:255
			OperatableStateMachine.add('Waitstate_4',
										self.use_behavior(WaitstateSM, 'Waitstate_4'),
										transitions={'Waited': 'Robot2toBin2'},
										autonomy={'Waited': Autonomy.Inherit})

			# x:470 y:687
			OperatableStateMachine.add('Waitstate_5',
										self.use_behavior(WaitstateSM, 'Waitstate_5'),
										transitions={'Waited': 'MoveR2toAgv2'},
										autonomy={'Waited': Autonomy.Inherit})

			# x:471 y:776
			OperatableStateMachine.add('Waitstate_6',
										self.use_behavior(WaitstateSM, 'Waitstate_6'),
										transitions={'Waited': 'MoveR2toHome2'},
										autonomy={'Waited': Autonomy.Inherit})

			# x:1372 y:637
			OperatableStateMachine.add('Waitstate_7',
										self.use_behavior(WaitstateSM, 'Waitstate_7'),
										transitions={'Waited': 'MoveR2toBin4'},
										autonomy={'Waited': Autonomy.Inherit})

			# x:1374 y:554
			OperatableStateMachine.add('Waitstate_8',
										self.use_behavior(WaitstateSM, 'Waitstate_8'),
										transitions={'Waited': 'MoveR1toHome2'},
										autonomy={'Waited': Autonomy.Inherit})

			# x:1378 y:391
			OperatableStateMachine.add('Waitstate_9',
										self.use_behavior(WaitstateSM, 'Waitstate_9'),
										transitions={'Waited': 'MoveR1toBin4'},
										autonomy={'Waited': Autonomy.Inherit})

			# x:891 y:324
			OperatableStateMachine.add('Waitstate_10',
										self.use_behavior(WaitstateSM, 'Waitstate_10'),
										transitions={'Waited': 'Robot1toBin5'},
										autonomy={'Waited': Autonomy.Inherit})

			# x:1520 y:171
			OperatableStateMachine.add('Waitstate_11',
										self.use_behavior(WaitstateSM, 'Waitstate_11'),
										transitions={'Waited': 'Robot1toBin6'},
										autonomy={'Waited': Autonomy.Inherit})

			# x:513 y:78
			OperatableStateMachine.add('Bin_1',
										EqualState(),
										transitions={'true': 'Robot2toBin1', 'false': 'Bin_2'},
										autonomy={'true': Autonomy.Off, 'false': Autonomy.Off},
										remapping={'value_a': 'bin_1', 'value_b': 'bin_location'})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
