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
Created on Wed May 13 2020
@author: Lein van Sluijs en Timon Korpershoek
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
		# x:990 y:841, x:824 y:33
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
			# x:33 y:121
			OperatableStateMachine.add('MoveR1Home1',
										SrdfStateToMoveitAriac(),
										transitions={'reached': 'MoveR2Home1', 'planning_failed': 'Waitstate_2', 'control_failed': 'Waitstate_2', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'move_home', 'move_group': 'move_group', 'move_group_prefix': 'robot_1', 'action_topic': 'action_topic', 'robot_name': 'robot_name', 'config_name_out': 'config_name_out', 'move_group_out': 'move_group_out', 'robot_name_out': 'robot_name_out', 'action_topic_out': 'action_topic_out', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:940 y:114
			OperatableStateMachine.add('Bin_5',
										EqualState(),
										transitions={'true': 'Robot1ToBin5', 'false': 'Bin_6'},
										autonomy={'true': Autonomy.Off, 'false': Autonomy.Off},
										remapping={'value_a': 'bin_location', 'value_b': 'bin_5'})

			# x:1275 y:109
			OperatableStateMachine.add('Bin_6',
										EqualState(),
										transitions={'true': 'Robot1ToBin6', 'false': 'Belt'},
										autonomy={'true': Autonomy.Off, 'false': Autonomy.Off},
										remapping={'value_a': 'bin_location', 'value_b': 'bin_6'})

			# x:1591 y:107
			OperatableStateMachine.add('Belt',
										EqualState(),
										transitions={'true': 'finished', 'false': 'failed'},
										autonomy={'true': Autonomy.Off, 'false': Autonomy.Off},
										remapping={'value_a': 'bin_location', 'value_b': 'belt'})

			# x:653 y:120
			OperatableStateMachine.add('Bin_2',
										EqualState(),
										transitions={'true': 'Robot2ToBin2', 'false': 'Bin_5'},
										autonomy={'true': Autonomy.Off, 'false': Autonomy.Off},
										remapping={'value_a': 'bin_location', 'value_b': 'bin_2'})

			# x:1276 y:202
			OperatableStateMachine.add('Robot1ToBin6',
										SrdfStateToMoveitAriac(),
										transitions={'reached': 'MoveR1Agv1', 'planning_failed': 'Waitstate_9', 'control_failed': 'Waitstate_9', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'move_bin6_1', 'move_group': 'move_group', 'move_group_prefix': 'robot_1', 'action_topic': 'action_topic', 'robot_name': 'robot_name', 'config_name_out': 'config_name_out', 'move_group_out': 'move_group_out', 'robot_name_out': 'robot_name_out', 'action_topic_out': 'action_topic_out', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:945 y:209
			OperatableStateMachine.add('Robot1ToBin5',
										SrdfStateToMoveitAriac(),
										transitions={'reached': 'MoveR1Agv1', 'planning_failed': 'Waitstate_8', 'control_failed': 'Waitstate_8', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'move_bin5_1', 'move_group': 'move_group', 'move_group_prefix': 'robot_1', 'action_topic': 'action_topic', 'robot_name': 'robot_name', 'config_name_out': 'config_name_out', 'move_group_out': 'move_group_out', 'robot_name_out': 'robot_name_out', 'action_topic_out': 'action_topic_out', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:669 y:209
			OperatableStateMachine.add('Robot2ToBin2',
										SrdfStateToMoveitAriac(),
										transitions={'reached': 'MoveR2Bin4', 'planning_failed': 'Waitstate_7', 'control_failed': 'failed', 'param_error': 'Waitstate_7'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'move_bin2_2', 'move_group': 'move_group', 'move_group_prefix': 'robot_2', 'action_topic': 'action_topic', 'robot_name': 'robot_name', 'config_name_out': 'config_name_out', 'move_group_out': 'move_group_out', 'robot_name_out': 'robot_name_out', 'action_topic_out': 'action_topic_out', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:407 y:210
			OperatableStateMachine.add('Robot2ToBin1',
										SrdfStateToMoveitAriac(),
										transitions={'reached': 'MoveR2Bin4', 'planning_failed': 'Waitstate_3', 'control_failed': 'Waitstate_3', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'move_bin1_2', 'move_group': 'move_group', 'move_group_prefix': 'robot_2', 'action_topic': 'action_topic', 'robot_name': 'robot_name', 'config_name_out': 'config_name_out', 'move_group_out': 'move_group_out', 'robot_name_out': 'robot_name_out', 'action_topic_out': 'action_topic_out', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:538 y:289
			OperatableStateMachine.add('MoveR2Bin4',
										SrdfStateToMoveitAriac(),
										transitions={'reached': 'MoveR2Home2', 'planning_failed': 'Waitstate_4', 'control_failed': 'Waitstate_4', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'move_bin4_2', 'move_group': 'move_group', 'move_group_prefix': 'robot_2', 'action_topic': 'action_topic', 'robot_name': 'robot_name', 'config_name_out': 'config_name_out', 'move_group_out': 'move_group_out', 'robot_name_out': 'robot_name_out', 'action_topic_out': 'action_topic_out', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:538 y:471
			OperatableStateMachine.add('MoveR1Bin4',
										SrdfStateToMoveitAriac(),
										transitions={'reached': 'MoveR1Agv1', 'planning_failed': 'Waitstate_6', 'control_failed': 'Waitstate_6', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'move_bin4_1', 'move_group': 'move_group', 'move_group_prefix': 'robot_1', 'action_topic': 'action_topic', 'robot_name': 'robot_name', 'config_name_out': 'config_name_out', 'move_group_out': 'move_group_out', 'robot_name_out': 'robot_name_out', 'action_topic_out': 'action_topic_out', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:538 y:381
			OperatableStateMachine.add('MoveR2Home2',
										SrdfStateToMoveitAriac(),
										transitions={'reached': 'MoveR1Bin4', 'planning_failed': 'Waitstate_4', 'control_failed': 'Waitstate_5', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'move_home', 'move_group': 'move_group', 'move_group_prefix': 'robot_2', 'action_topic': 'action_topic', 'robot_name': 'robot_name', 'config_name_out': 'config_name_out', 'move_group_out': 'move_group_out', 'robot_name_out': 'robot_name_out', 'action_topic_out': 'action_topic_out', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:939 y:617
			OperatableStateMachine.add('MoveR1Agv1',
										SrdfStateToMoveitAriac(),
										transitions={'reached': 'MoveR1Home2', 'planning_failed': 'Waitstate_10', 'control_failed': 'Waitstate_10', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'move_agv1', 'move_group': 'move_group', 'move_group_prefix': 'robot_1', 'action_topic': 'action_topic', 'robot_name': 'robot_name', 'config_name_out': 'config_name_out', 'move_group_out': 'move_group_out', 'robot_name_out': 'robot_name_out', 'action_topic_out': 'action_topic_out', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:939 y:729
			OperatableStateMachine.add('MoveR1Home2',
										SrdfStateToMoveitAriac(),
										transitions={'reached': 'finished', 'planning_failed': 'Waitstate_11', 'control_failed': 'Waitstate_11', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'move_home', 'move_group': 'move_group', 'move_group_prefix': 'robot_1', 'action_topic': 'action_topic', 'robot_name': 'robot_name', 'config_name_out': 'config_name_out', 'move_group_out': 'move_group_out', 'robot_name_out': 'robot_name_out', 'action_topic_out': 'action_topic_out', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:201 y:122
			OperatableStateMachine.add('MoveR2Home1',
										SrdfStateToMoveitAriac(),
										transitions={'reached': 'Bin_1', 'planning_failed': 'Waitstate', 'control_failed': 'Waitstate', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'move_home', 'move_group': 'move_group', 'move_group_prefix': 'robot_2', 'action_topic': 'action_topic', 'robot_name': 'robot_name', 'config_name_out': 'config_name_out', 'move_group_out': 'move_group_out', 'robot_name_out': 'robot_name_out', 'action_topic_out': 'action_topic_out', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:401 y:122
			OperatableStateMachine.add('Bin_1',
										EqualState(),
										transitions={'true': 'Robot2ToBin1', 'false': 'Bin_2'},
										autonomy={'true': Autonomy.Off, 'false': Autonomy.Off},
										remapping={'value_a': 'bin_location', 'value_b': 'bin_1'})

			# x:186 y:231
			OperatableStateMachine.add('Waitstate',
										self.use_behavior(WaitstateSM, 'Waitstate'),
										transitions={'Waited': 'MoveR2Home1'},
										autonomy={'Waited': Autonomy.Inherit})

			# x:18 y:229
			OperatableStateMachine.add('Waitstate_2',
										self.use_behavior(WaitstateSM, 'Waitstate_2'),
										transitions={'Waited': 'MoveR1Home1'},
										autonomy={'Waited': Autonomy.Inherit})

			# x:185 y:304
			OperatableStateMachine.add('Waitstate_3',
										self.use_behavior(WaitstateSM, 'Waitstate_3'),
										transitions={'Waited': 'Robot2ToBin1'},
										autonomy={'Waited': Autonomy.Inherit})

			# x:362 y:308
			OperatableStateMachine.add('Waitstate_4',
										self.use_behavior(WaitstateSM, 'Waitstate_4'),
										transitions={'Waited': 'Waitstate_3'},
										autonomy={'Waited': Autonomy.Inherit})

			# x:360 y:385
			OperatableStateMachine.add('Waitstate_5',
										self.use_behavior(WaitstateSM, 'Waitstate_5'),
										transitions={'Waited': 'MoveR2Home2'},
										autonomy={'Waited': Autonomy.Inherit})

			# x:359 y:466
			OperatableStateMachine.add('Waitstate_6',
										self.use_behavior(WaitstateSM, 'Waitstate_6'),
										transitions={'Waited': 'MoveR1Bin4'},
										autonomy={'Waited': Autonomy.Inherit})

			# x:697 y:284
			OperatableStateMachine.add('Waitstate_7',
										self.use_behavior(WaitstateSM, 'Waitstate_7'),
										transitions={'Waited': 'Robot2ToBin2'},
										autonomy={'Waited': Autonomy.Inherit})

			# x:1044 y:276
			OperatableStateMachine.add('Waitstate_8',
										self.use_behavior(WaitstateSM, 'Waitstate_8'),
										transitions={'Waited': 'Robot1ToBin5'},
										autonomy={'Waited': Autonomy.Inherit})

			# x:1498 y:192
			OperatableStateMachine.add('Waitstate_9',
										self.use_behavior(WaitstateSM, 'Waitstate_9'),
										transitions={'Waited': 'Robot1ToBin6'},
										autonomy={'Waited': Autonomy.Inherit})

			# x:677 y:644
			OperatableStateMachine.add('Waitstate_10',
										self.use_behavior(WaitstateSM, 'Waitstate_10'),
										transitions={'Waited': 'MoveR1Agv1'},
										autonomy={'Waited': Autonomy.Inherit})

			# x:679 y:742
			OperatableStateMachine.add('Waitstate_11',
										self.use_behavior(WaitstateSM, 'Waitstate_11'),
										transitions={'Waited': 'MoveR1Home2'},
										autonomy={'Waited': Autonomy.Inherit})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
