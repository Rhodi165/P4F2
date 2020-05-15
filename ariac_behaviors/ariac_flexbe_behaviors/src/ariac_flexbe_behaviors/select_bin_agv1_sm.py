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
from ariac_flexbe_states.detect_part_camera_ariac_state import DetectPartCameraAriacState
from ariac_flexbe_states.compute_grasp_ariac_state import ComputeGraspAriacState
from ariac_flexbe_states.moveit_to_joints_dyn_ariac_state import MoveitToJointsDynAriacState
from ariac_flexbe_states.gripper import VacuumGripperControlState
from ariac_flexbe_states.compute_grasp_partoffset_ariac_state import ComputeGraspPartOffsetAriacState
from ariac_flexbe_states.get_object_pose import GetObjectPoseState
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
		self.add_behavior(WaitstateSM, 'Waitstate_9_2')
		self.add_behavior(WaitstateSM, 'Waitstate_8_2')
		self.add_behavior(WaitstateSM, 'Waitstate_7_2')
		self.add_behavior(WaitstateSM, 'Waitstate_3_2')
		self.add_behavior(WaitstateSM, 'Waitstate_6_2')

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		# x:1748 y:879, x:903 y:11
		_state_machine = OperatableStateMachine(outcomes=['finished', 'failed'], input_keys=['part_type', 'pose_on_agv', 'bin_location'])
		_state_machine.userdata.part_type = ''
		_state_machine.userdata.pose_on_agv = []
		_state_machine.userdata.bin_1 = 'bin1'
		_state_machine.userdata.bin_2 = 'bin2'
		_state_machine.userdata.bin_5 = 'bin5'
		_state_machine.userdata.bin_6 = 'bin6'
		_state_machine.userdata.belt = 'belt'
		_state_machine.userdata.bin_location = ''
		_state_machine.userdata.move_bin6_1 = 'bin1_1PreGrasp'
		_state_machine.userdata.move_group = 'manipulator'
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
		_state_machine.userdata.Robot1_ref_frame = 'arm1_linear_arm_actuator'
		_state_machine.userdata.camera_topic_2 = '/ariac/logical_camera_drijfstang'
		_state_machine.userdata.camera_topic_3 = '/ariac/logical_camera_binR'
		_state_machine.userdata.camera_topic_4 = '/ariac/logical_camera_binL'
		_state_machine.userdata.camera_topic_5 = '/ariac/logical_camera_pulley'
		_state_machine.userdata.camera_topic_6 = '/ariac/logical_camera_pakking'
		_state_machine.userdata.camera_topic_agv1 = '/ariac/logical_camera_agvL'
		_state_machine.userdata.camera_topic_agv2 = '/ariac/logical_camera_agvR'
		_state_machine.userdata.camera_topic_1 = '/ariac/logical_camera_tandwiel'
		_state_machine.userdata.camera_frame_2 = 'logical_camera_drijfstang_frame'
		_state_machine.userdata.camera_frame_3 = 'logical_camera_binR_frame'
		_state_machine.userdata.camera_frame_4 = 'logical_camera_binL_frame'
		_state_machine.userdata.camera_frame_5 = 'logical_camera_pulley_frame'
		_state_machine.userdata.camera_frame_6 = 'logical_camera_pakking_frame'
		_state_machine.userdata.camera_frame_agv1 = 'logical_camera_agvL_frame'
		_state_machine.userdata.camera_frame_agv2 = 'logical_camera_agvR_frame'
		_state_machine.userdata.camera_frame_1 = 'logical_camera_tandwiel_frame'
		_state_machine.userdata.Robot2_ref_frame = 'arm2_linear_arm_actuator'
		_state_machine.userdata.tool_link = 'ee_link'
		_state_machine.userdata.offset_gasket = 0.029
		_state_machine.userdata.rotation = 0
		_state_machine.userdata.move_group_prefix1 = '/ariac/arm1'
		_state_machine.userdata.move_group_prefix2 = '/ariac/arm2'
		_state_machine.userdata.arm_id1 = 'arm1'
		_state_machine.userdata.arm_id2 = 'arm2'
		_state_machine.userdata.offset_agv = 0.12
		_state_machine.userdata.poseagv = ''
		_state_machine.userdata.offset_pulley = 0.08
		_state_machine.userdata.offset_drijfstang = 0.019
		_state_machine.userdata.offset_tandwiel = 0.025

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]


		with _state_machine:
			# x:47 y:23
			OperatableStateMachine.add('MoveR1Home1',
										SrdfStateToMoveitAriac(),
										transitions={'reached': 'MoveR2Home1', 'planning_failed': 'Waitstate_2', 'control_failed': 'Waitstate_2', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'move_home', 'move_group': 'move_group', 'move_group_prefix': 'robot_1', 'action_topic': 'action_topic', 'robot_name': 'robot_name', 'config_name_out': 'config_name_out', 'move_group_out': 'move_group_out', 'robot_name_out': 'robot_name_out', 'action_topic_out': 'action_topic_out', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:1445 y:31
			OperatableStateMachine.add('Bin_6',
										EqualState(),
										transitions={'true': 'DetectGasket', 'false': 'Belt'},
										autonomy={'true': Autonomy.Off, 'false': Autonomy.Off},
										remapping={'value_a': 'bin_location', 'value_b': 'bin_6'})

			# x:1664 y:27
			OperatableStateMachine.add('Belt',
										EqualState(),
										transitions={'true': 'finished', 'false': 'failed'},
										autonomy={'true': Autonomy.Off, 'false': Autonomy.Off},
										remapping={'value_a': 'bin_location', 'value_b': 'belt'})

			# x:850 y:45
			OperatableStateMachine.add('Bin_2',
										EqualState(),
										transitions={'true': 'Detectdrijfstang', 'false': 'Bin_5'},
										autonomy={'true': Autonomy.Off, 'false': Autonomy.Off},
										remapping={'value_a': 'bin_location', 'value_b': 'bin_2'})

			# x:1457 y:192
			OperatableStateMachine.add('Robot1ToBin6',
										SrdfStateToMoveitAriac(),
										transitions={'reached': 'ComputePick', 'planning_failed': 'Waitstate_9', 'control_failed': 'Waitstate_9', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'move_bin6_1', 'move_group': 'move_group', 'move_group_prefix': 'robot_1', 'action_topic': 'action_topic', 'robot_name': 'robot_name', 'config_name_out': 'config_name_out', 'move_group_out': 'move_group_out', 'robot_name_out': 'robot_name_out', 'action_topic_out': 'action_topic_out', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:1143 y:188
			OperatableStateMachine.add('Robot1ToBin5',
										SrdfStateToMoveitAriac(),
										transitions={'reached': 'ComputePick_2', 'planning_failed': 'Waitstate_8', 'control_failed': 'Waitstate_8', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'move_bin5_1', 'move_group': 'move_group', 'move_group_prefix': 'robot_1', 'action_topic': 'action_topic', 'robot_name': 'robot_name', 'config_name_out': 'config_name_out', 'move_group_out': 'move_group_out', 'robot_name_out': 'robot_name_out', 'action_topic_out': 'action_topic_out', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:837 y:196
			OperatableStateMachine.add('Robot2ToBin2',
										SrdfStateToMoveitAriac(),
										transitions={'reached': 'ComputePick_2_2', 'planning_failed': 'Waitstate_7', 'control_failed': 'Waitstate_7', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'move_bin2_2', 'move_group': 'move_group', 'move_group_prefix': 'robot_2', 'action_topic': 'action_topic', 'robot_name': 'robot_name', 'config_name_out': 'config_name_out', 'move_group_out': 'move_group_out', 'robot_name_out': 'robot_name_out', 'action_topic_out': 'action_topic_out', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:395 y:192
			OperatableStateMachine.add('Robot2ToBin1',
										SrdfStateToMoveitAriac(),
										transitions={'reached': 'ComputePick_2_2_2', 'planning_failed': 'Waitstate_3', 'control_failed': 'Waitstate_3', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'move_bin1_2', 'move_group': 'move_group', 'move_group_prefix': 'robot_2', 'action_topic': 'action_topic', 'robot_name': 'robot_name', 'config_name_out': 'config_name_out', 'move_group_out': 'move_group_out', 'robot_name_out': 'robot_name_out', 'action_topic_out': 'action_topic_out', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:662 y:179
			OperatableStateMachine.add('MoveR2Bin4',
										SrdfStateToMoveitAriac(),
										transitions={'reached': 'GripperOff_2', 'planning_failed': 'Waitstate_4', 'control_failed': 'Waitstate_4', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'move_bin4_2', 'move_group': 'move_group', 'move_group_prefix': 'robot_2', 'action_topic': 'action_topic', 'robot_name': 'robot_name', 'config_name_out': 'config_name_out', 'move_group_out': 'move_group_out', 'robot_name_out': 'robot_name_out', 'action_topic_out': 'action_topic_out', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:485 y:435
			OperatableStateMachine.add('MoveR1Bin4',
										SrdfStateToMoveitAriac(),
										transitions={'reached': 'ComputePick_2_2_3', 'planning_failed': 'Waitstate_6', 'control_failed': 'Waitstate_6', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'move_bin4_1', 'move_group': 'move_group', 'move_group_prefix': 'robot_1', 'action_topic': 'action_topic', 'robot_name': 'robot_name', 'config_name_out': 'config_name_out', 'move_group_out': 'move_group_out', 'robot_name_out': 'robot_name_out', 'action_topic_out': 'action_topic_out', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:661 y:328
			OperatableStateMachine.add('MoveR2Home2',
										SrdfStateToMoveitAriac(),
										transitions={'reached': 'Detectdrijfstang_3', 'planning_failed': 'Waitstate_5', 'control_failed': 'Waitstate_5', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'move_home', 'move_group': 'move_group', 'move_group_prefix': 'robot_2', 'action_topic': 'action_topic', 'robot_name': 'robot_name', 'config_name_out': 'config_name_out', 'move_group_out': 'move_group_out', 'robot_name_out': 'robot_name_out', 'action_topic_out': 'action_topic_out', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:939 y:617
			OperatableStateMachine.add('MoveR1Agv1',
										SrdfStateToMoveitAriac(),
										transitions={'reached': 'getagv1loc', 'planning_failed': 'Waitstate_10', 'control_failed': 'Waitstate_10', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'move_agv1', 'move_group': 'move_group', 'move_group_prefix': 'robot_1', 'action_topic': 'action_topic', 'robot_name': 'robot_name', 'config_name_out': 'config_name_out', 'move_group_out': 'move_group_out', 'robot_name_out': 'robot_name_out', 'action_topic_out': 'action_topic_out', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:1585 y:860
			OperatableStateMachine.add('MoveR1Home2',
										SrdfStateToMoveitAriac(),
										transitions={'reached': 'finished', 'planning_failed': 'Waitstate_11', 'control_failed': 'Waitstate_11', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'move_home', 'move_group': 'move_group', 'move_group_prefix': 'robot_1', 'action_topic': 'action_topic', 'robot_name': 'robot_name', 'config_name_out': 'config_name_out', 'move_group_out': 'move_group_out', 'robot_name_out': 'robot_name_out', 'action_topic_out': 'action_topic_out', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:201 y:22
			OperatableStateMachine.add('MoveR2Home1',
										SrdfStateToMoveitAriac(),
										transitions={'reached': 'Bin_1', 'planning_failed': 'Waitstate', 'control_failed': 'Waitstate', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'move_home', 'move_group': 'move_group', 'move_group_prefix': 'robot_2', 'action_topic': 'action_topic', 'robot_name': 'robot_name', 'config_name_out': 'config_name_out', 'move_group_out': 'move_group_out', 'robot_name_out': 'robot_name_out', 'action_topic_out': 'action_topic_out', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:395 y:24
			OperatableStateMachine.add('Bin_1',
										EqualState(),
										transitions={'true': 'Detecttandwiel', 'false': 'Bin_2'},
										autonomy={'true': Autonomy.Off, 'false': Autonomy.Off},
										remapping={'value_a': 'bin_location', 'value_b': 'bin_1'})

			# x:188 y:96
			OperatableStateMachine.add('Waitstate',
										self.use_behavior(WaitstateSM, 'Waitstate'),
										transitions={'Waited': 'MoveR2Home1'},
										autonomy={'Waited': Autonomy.Inherit})

			# x:11 y:124
			OperatableStateMachine.add('Waitstate_2',
										self.use_behavior(WaitstateSM, 'Waitstate_2'),
										transitions={'Waited': 'MoveR1Home1'},
										autonomy={'Waited': Autonomy.Inherit})

			# x:178 y:159
			OperatableStateMachine.add('Waitstate_3',
										self.use_behavior(WaitstateSM, 'Waitstate_3'),
										transitions={'Waited': 'Robot2ToBin1'},
										autonomy={'Waited': Autonomy.Inherit})

			# x:648 y:86
			OperatableStateMachine.add('Waitstate_4',
										self.use_behavior(WaitstateSM, 'Waitstate_4'),
										transitions={'Waited': 'MoveR2Bin4'},
										autonomy={'Waited': Autonomy.Inherit})

			# x:482 y:323
			OperatableStateMachine.add('Waitstate_5',
										self.use_behavior(WaitstateSM, 'Waitstate_5'),
										transitions={'Waited': 'MoveR2Home2'},
										autonomy={'Waited': Autonomy.Inherit})

			# x:291 y:432
			OperatableStateMachine.add('Waitstate_6',
										self.use_behavior(WaitstateSM, 'Waitstate_6'),
										transitions={'Waited': 'MoveR1Bin4'},
										autonomy={'Waited': Autonomy.Inherit})

			# x:987 y:190
			OperatableStateMachine.add('Waitstate_7',
										self.use_behavior(WaitstateSM, 'Waitstate_7'),
										transitions={'Waited': 'Robot2ToBin2'},
										autonomy={'Waited': Autonomy.Inherit})

			# x:1300 y:186
			OperatableStateMachine.add('Waitstate_8',
										self.use_behavior(WaitstateSM, 'Waitstate_8'),
										transitions={'Waited': 'Robot1ToBin5'},
										autonomy={'Waited': Autonomy.Inherit})

			# x:1661 y:188
			OperatableStateMachine.add('Waitstate_9',
										self.use_behavior(WaitstateSM, 'Waitstate_9'),
										transitions={'Waited': 'Robot1ToBin6'},
										autonomy={'Waited': Autonomy.Inherit})

			# x:677 y:644
			OperatableStateMachine.add('Waitstate_10',
										self.use_behavior(WaitstateSM, 'Waitstate_10'),
										transitions={'Waited': 'MoveR1Agv1'},
										autonomy={'Waited': Autonomy.Inherit})

			# x:1575 y:772
			OperatableStateMachine.add('Waitstate_11',
										self.use_behavior(WaitstateSM, 'Waitstate_11'),
										transitions={'Waited': 'MoveR1Home2'},
										autonomy={'Waited': Autonomy.Inherit})

			# x:1128 y:36
			OperatableStateMachine.add('Bin_5',
										EqualState(),
										transitions={'true': 'Detectpulley', 'false': 'Bin_6'},
										autonomy={'true': Autonomy.Off, 'false': Autonomy.Off},
										remapping={'value_a': 'bin_location', 'value_b': 'bin_5'})

			# x:1441 y:118
			OperatableStateMachine.add('DetectGasket',
										DetectPartCameraAriacState(time_out=0.5),
										transitions={'continue': 'Robot1ToBin6', 'failed': 'failed', 'not_found': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off, 'not_found': Autonomy.Off},
										remapping={'ref_frame': 'Robot1_ref_frame', 'camera_topic': 'camera_topic_6', 'camera_frame': 'camera_frame_6', 'part': 'part_type', 'pose': 'pose'})

			# x:1455 y:274
			OperatableStateMachine.add('ComputePick',
										ComputeGraspAriacState(joint_names=['linear_arm_actuator_joint', 'shoulder_pan_joint', 'shoulder_lift_joint', 'elbow_joint', 'wrist_1_joint', 'wrist_2_joint', 'wrist_3_joint']),
										transitions={'continue': 'MoveR1toPick', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'move_group': 'move_group', 'move_group_prefix': 'move_group_prefix1', 'tool_link': 'tool_link', 'pose': 'pose', 'offset': 'offset_gasket', 'rotation': 'rotation', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:1445 y:349
			OperatableStateMachine.add('MoveR1toPick',
										MoveitToJointsDynAriacState(),
										transitions={'reached': 'GripperOn', 'planning_failed': 'failed', 'control_failed': 'GripperOn'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off},
										remapping={'move_group_prefix': 'move_group_prefix1', 'move_group': 'move_group', 'action_topic': 'action_topic', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:1447 y:435
			OperatableStateMachine.add('GripperOn',
										VacuumGripperControlState(enable=True),
										transitions={'continue': 'Robot1ToBin6_2', 'failed': 'failed', 'invalid_arm_id': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off, 'invalid_arm_id': Autonomy.Off},
										remapping={'arm_id': 'arm_id1'})

			# x:943 y:850
			OperatableStateMachine.add('computegrasp',
										ComputeGraspPartOffsetAriacState(joint_names=['linear_arm_actuator_joint', 'shoulder_pan_joint', 'shoulder_lift_joint', 'elbow_joint', 'wrist_1_joint', 'wrist_2_joint', 'wrist_3_joint']),
										transitions={'continue': 'MoveR1toPick_2', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'move_group': 'move_group', 'move_group_prefix': 'move_group_prefix1', 'tool_link': 'tool_link', 'pose': 'poseagv', 'offset': 'offset_agv', 'rotation': 'rotation', 'part_pose': 'pose_on_agv', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:1384 y:858
			OperatableStateMachine.add('GripperOff',
										VacuumGripperControlState(enable=False),
										transitions={'continue': 'MoveR1Home2', 'failed': 'failed', 'invalid_arm_id': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off, 'invalid_arm_id': Autonomy.Off},
										remapping={'arm_id': 'arm_id1'})

			# x:939 y:756
			OperatableStateMachine.add('getagv1loc',
										GetObjectPoseState(object_frame='kit_tray_1', ref_frame='arm1_linear_arm_actuator'),
										transitions={'continue': 'computegrasp', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'pose': 'poseagv'})

			# x:1180 y:854
			OperatableStateMachine.add('MoveR1toPick_2',
										MoveitToJointsDynAriacState(),
										transitions={'reached': 'GripperOff', 'planning_failed': 'failed', 'control_failed': 'GripperOff'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off},
										remapping={'move_group_prefix': 'move_group_prefix1', 'move_group': 'move_group', 'action_topic': 'action_topic', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:1129 y:108
			OperatableStateMachine.add('Detectpulley',
										DetectPartCameraAriacState(time_out=0.5),
										transitions={'continue': 'Robot1ToBin5', 'failed': 'failed', 'not_found': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off, 'not_found': Autonomy.Off},
										remapping={'ref_frame': 'Robot1_ref_frame', 'camera_topic': 'camera_topic_5', 'camera_frame': 'camera_frame_5', 'part': 'part_type', 'pose': 'pose'})

			# x:1141 y:273
			OperatableStateMachine.add('ComputePick_2',
										ComputeGraspAriacState(joint_names=['linear_arm_actuator_joint', 'shoulder_pan_joint', 'shoulder_lift_joint', 'elbow_joint', 'wrist_1_joint', 'wrist_2_joint', 'wrist_3_joint']),
										transitions={'continue': 'MoveR1toPick_4', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'move_group': 'move_group', 'move_group_prefix': 'move_group_prefix1', 'tool_link': 'tool_link', 'pose': 'pose', 'offset': 'offset_pulley', 'rotation': 'rotation', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:1131 y:352
			OperatableStateMachine.add('MoveR1toPick_4',
										MoveitToJointsDynAriacState(),
										transitions={'reached': 'GripperOn_2', 'planning_failed': 'failed', 'control_failed': 'GripperOn_2'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off},
										remapping={'move_group_prefix': 'move_group_prefix1', 'move_group': 'move_group', 'action_topic': 'action_topic', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:1125 y:428
			OperatableStateMachine.add('GripperOn_2',
										VacuumGripperControlState(enable=True),
										transitions={'continue': 'Robot1ToBin5_2', 'failed': 'failed', 'invalid_arm_id': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off, 'invalid_arm_id': Autonomy.Off},
										remapping={'arm_id': 'arm_id1'})

			# x:857 y:107
			OperatableStateMachine.add('Detectdrijfstang',
										DetectPartCameraAriacState(time_out=0.5),
										transitions={'continue': 'Robot2ToBin2', 'failed': 'failed', 'not_found': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off, 'not_found': Autonomy.Off},
										remapping={'ref_frame': 'Robot2_ref_frame', 'camera_topic': 'camera_topic_2', 'camera_frame': 'camera_frame_2', 'part': 'part_type', 'pose': 'pose'})

			# x:851 y:261
			OperatableStateMachine.add('ComputePick_2_2',
										ComputeGraspAriacState(joint_names=['linear_arm_actuator_joint', 'shoulder_pan_joint', 'shoulder_lift_joint', 'elbow_joint', 'wrist_1_joint', 'wrist_2_joint', 'wrist_3_joint']),
										transitions={'continue': 'MoveR2toPick_4_2', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'move_group': 'move_group', 'move_group_prefix': 'move_group_prefix2', 'tool_link': 'tool_link', 'pose': 'pose', 'offset': 'offset_drijfstang', 'rotation': 'rotation', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:856 y:336
			OperatableStateMachine.add('MoveR2toPick_4_2',
										MoveitToJointsDynAriacState(),
										transitions={'reached': 'GripperOn_2_2', 'planning_failed': 'failed', 'control_failed': 'GripperOn_2_2'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off},
										remapping={'move_group_prefix': 'move_group_prefix2', 'move_group': 'move_group', 'action_topic': 'action_topic', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:860 y:412
			OperatableStateMachine.add('GripperOn_2_2',
										VacuumGripperControlState(enable=True),
										transitions={'continue': 'Robot2ToBin2_2', 'failed': 'failed', 'invalid_arm_id': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off, 'invalid_arm_id': Autonomy.Off},
										remapping={'arm_id': 'arm_id2'})

			# x:372 y:101
			OperatableStateMachine.add('Detecttandwiel',
										DetectPartCameraAriacState(time_out=0.5),
										transitions={'continue': 'Robot2ToBin1', 'failed': 'failed', 'not_found': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off, 'not_found': Autonomy.Off},
										remapping={'ref_frame': 'Robot2_ref_frame', 'camera_topic': 'camera_topic_1', 'camera_frame': 'camera_frame_1', 'part': 'part_type', 'pose': 'pose'})

			# x:229 y:227
			OperatableStateMachine.add('ComputePick_2_2_2',
										ComputeGraspAriacState(joint_names=['linear_arm_actuator_joint', 'shoulder_pan_joint', 'shoulder_lift_joint', 'elbow_joint', 'wrist_1_joint', 'wrist_2_joint', 'wrist_3_joint']),
										transitions={'continue': 'MoveR2toPick_4_2_2', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'move_group': 'move_group', 'move_group_prefix': 'move_group_prefix2', 'tool_link': 'tool_link', 'pose': 'pose', 'offset': 'offset_tandwiel', 'rotation': 'rotation', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:47 y:245
			OperatableStateMachine.add('MoveR2toPick_4_2_2',
										MoveitToJointsDynAriacState(),
										transitions={'reached': 'GripperOn_2_2_2', 'planning_failed': 'failed', 'control_failed': 'GripperOn_2_2_2'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off},
										remapping={'move_group_prefix': 'move_group_prefix1', 'move_group': 'move_group', 'action_topic': 'action_topic', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:51 y:333
			OperatableStateMachine.add('GripperOn_2_2_2',
										VacuumGripperControlState(enable=True),
										transitions={'continue': 'Robot2ToBin1_2', 'failed': 'failed', 'invalid_arm_id': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off, 'invalid_arm_id': Autonomy.Off},
										remapping={'arm_id': 'arm_id2'})

			# x:641 y:261
			OperatableStateMachine.add('GripperOff_2',
										VacuumGripperControlState(enable=False),
										transitions={'continue': 'MoveR2Home2', 'failed': 'failed', 'invalid_arm_id': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off, 'invalid_arm_id': Autonomy.Off},
										remapping={'arm_id': 'arm_id2'})

			# x:650 y:404
			OperatableStateMachine.add('Detectdrijfstang_3',
										DetectPartCameraAriacState(time_out=0.5),
										transitions={'continue': 'MoveR1Bin4', 'failed': 'failed', 'not_found': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off, 'not_found': Autonomy.Off},
										remapping={'ref_frame': 'Robot1_ref_frame', 'camera_topic': 'camera_topic_4', 'camera_frame': 'camera_frame_4', 'part': 'part_type', 'pose': 'pose'})

			# x:381 y:511
			OperatableStateMachine.add('ComputePick_2_2_3',
										ComputeGraspAriacState(joint_names=['linear_arm_actuator_joint', 'shoulder_pan_joint', 'shoulder_lift_joint', 'elbow_joint', 'wrist_1_joint', 'wrist_2_joint', 'wrist_3_joint']),
										transitions={'continue': 'MoveR1toPick_4_2_3', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'move_group': 'move_group', 'move_group_prefix': 'move_group_prefix1', 'tool_link': 'tool_link', 'pose': 'pose', 'offset': 'offset_drijfstang', 'rotation': 'rotation', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:360 y:605
			OperatableStateMachine.add('MoveR1toPick_4_2_3',
										MoveitToJointsDynAriacState(),
										transitions={'reached': 'GripperOn_2_2_3', 'planning_failed': 'failed', 'control_failed': 'GripperOn_2_2_3'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off},
										remapping={'move_group_prefix': 'move_group_prefix1', 'move_group': 'move_group', 'action_topic': 'action_topic', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:358 y:704
			OperatableStateMachine.add('GripperOn_2_2_3',
										VacuumGripperControlState(enable=True),
										transitions={'continue': 'MoveR1Bin4_2', 'failed': 'failed', 'invalid_arm_id': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off, 'invalid_arm_id': Autonomy.Off},
										remapping={'arm_id': 'arm_id1'})

			# x:1449 y:527
			OperatableStateMachine.add('Robot1ToBin6_2',
										SrdfStateToMoveitAriac(),
										transitions={'reached': 'MoveR1Agv1', 'planning_failed': 'Waitstate_9_2', 'control_failed': 'Waitstate_9_2', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'move_bin6_1', 'move_group': 'move_group', 'move_group_prefix': 'robot_1', 'action_topic': 'action_topic', 'robot_name': 'robot_name', 'config_name_out': 'config_name_out', 'move_group_out': 'move_group_out', 'robot_name_out': 'robot_name_out', 'action_topic_out': 'action_topic_out', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:1632 y:517
			OperatableStateMachine.add('Waitstate_9_2',
										self.use_behavior(WaitstateSM, 'Waitstate_9_2'),
										transitions={'Waited': 'Robot1ToBin6_2'},
										autonomy={'Waited': Autonomy.Inherit})

			# x:1108 y:511
			OperatableStateMachine.add('Robot1ToBin5_2',
										SrdfStateToMoveitAriac(),
										transitions={'reached': 'MoveR1Agv1', 'planning_failed': 'Waitstate_8_2', 'control_failed': 'Waitstate_8_2', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'move_bin5_1', 'move_group': 'move_group', 'move_group_prefix': 'robot_1', 'action_topic': 'action_topic', 'robot_name': 'robot_name', 'config_name_out': 'config_name_out', 'move_group_out': 'move_group_out', 'robot_name_out': 'robot_name_out', 'action_topic_out': 'action_topic_out', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:1267 y:506
			OperatableStateMachine.add('Waitstate_8_2',
										self.use_behavior(WaitstateSM, 'Waitstate_8_2'),
										transitions={'Waited': 'Robot1ToBin5_2'},
										autonomy={'Waited': Autonomy.Inherit})

			# x:739 y:503
			OperatableStateMachine.add('Robot2ToBin2_2',
										SrdfStateToMoveitAriac(),
										transitions={'reached': 'MoveR2Bin4', 'planning_failed': 'Waitstate_7_2', 'control_failed': 'Waitstate_7_2', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'move_bin2_2', 'move_group': 'move_group', 'move_group_prefix': 'robot_2', 'action_topic': 'action_topic', 'robot_name': 'robot_name', 'config_name_out': 'config_name_out', 'move_group_out': 'move_group_out', 'robot_name_out': 'robot_name_out', 'action_topic_out': 'action_topic_out', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:916 y:505
			OperatableStateMachine.add('Waitstate_7_2',
										self.use_behavior(WaitstateSM, 'Waitstate_7_2'),
										transitions={'Waited': 'Robot2ToBin2_2'},
										autonomy={'Waited': Autonomy.Inherit})

			# x:261 y:333
			OperatableStateMachine.add('Robot2ToBin1_2',
										SrdfStateToMoveitAriac(),
										transitions={'reached': 'MoveR2Bin4', 'planning_failed': 'Waitstate_3_2', 'control_failed': 'Waitstate_3_2', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'move_bin1_2', 'move_group': 'move_group', 'move_group_prefix': 'robot_2', 'action_topic': 'action_topic', 'robot_name': 'robot_name', 'config_name_out': 'config_name_out', 'move_group_out': 'move_group_out', 'robot_name_out': 'robot_name_out', 'action_topic_out': 'action_topic_out', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:58 y:486
			OperatableStateMachine.add('Waitstate_3_2',
										self.use_behavior(WaitstateSM, 'Waitstate_3_2'),
										transitions={'Waited': 'Robot2ToBin1_2'},
										autonomy={'Waited': Autonomy.Inherit})

			# x:553 y:784
			OperatableStateMachine.add('MoveR1Bin4_2',
										SrdfStateToMoveitAriac(),
										transitions={'reached': 'MoveR1Agv1', 'planning_failed': 'Waitstate_6_2', 'control_failed': 'Waitstate_6_2', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'move_bin4_1', 'move_group': 'move_group', 'move_group_prefix': 'robot_1', 'action_topic': 'action_topic', 'robot_name': 'robot_name', 'config_name_out': 'config_name_out', 'move_group_out': 'move_group_out', 'robot_name_out': 'robot_name_out', 'action_topic_out': 'action_topic_out', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:753 y:799
			OperatableStateMachine.add('Waitstate_6_2',
										self.use_behavior(WaitstateSM, 'Waitstate_6_2'),
										transitions={'Waited': 'MoveR1Bin4_2'},
										autonomy={'Waited': Autonomy.Inherit})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
