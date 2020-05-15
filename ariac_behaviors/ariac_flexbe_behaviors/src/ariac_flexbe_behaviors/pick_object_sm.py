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
from ariac_flexbe_states.detect_part_camera_ariac_state import DetectPartCameraAriacState
from ariac_flexbe_states.compute_grasp_ariac_state import ComputeGraspAriacState
from ariac_flexbe_states.message_state import MessageState
# Additional imports can be added inside the following tags
# [MANUAL_IMPORT]

# [/MANUAL_IMPORT]


'''
Created on Fri May 15 2020
@author: Lein en Timon
'''
class Pick_objectSM(Behavior):
	'''
	state to pick the object
	'''


	def __init__(self):
		super(Pick_objectSM, self).__init__()
		self.name = 'Pick_object'

		# parameters of this behavior

		# references to used behaviors

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		# x:806 y:705, x:800 y:403
		_state_machine = OperatableStateMachine(outcomes=['finished', 'failed'], input_keys=['bin_location', 'part_type'])
		_state_machine.userdata.bin_location = ''
		_state_machine.userdata.robot_1 = '/ariac/arm1'
		_state_machine.userdata.robot_2 = '/ariac/arm2'
		_state_machine.userdata.action_topic = '/move_group'
		_state_machine.userdata.robot_name = ''
		_state_machine.userdata.move_group = ''
		_state_machine.userdata.camera_ref_frame1 = 'arm1_linear_arm_actuator'
		_state_machine.userdata.camera_topic_1 = '/ariac/logical_camera_tandwiel'
		_state_machine.userdata.camera_topic_3 = '/ariac/logical_camera_binR'
		_state_machine.userdata.camera_topic_2 = '/ariac/logical_camera_drijfstang'
		_state_machine.userdata.camera_topic_4 = '/ariac/logical_camera_binL'
		_state_machine.userdata.camera_topic_5 = '/ariac/logical_camera_pulley'
		_state_machine.userdata.camera_topic_6 = '/ariac/logical_camera_pakking'
		_state_machine.userdata.camera_topic_agv1 = '/ariac/logical_camera_agvL'
		_state_machine.userdata.camera_topic_agv2 = '/ariac/logical_camera_agvR'
		_state_machine.userdata.tool_link = 'ee_link'
		_state_machine.userdata.bin_1 = 'bin1'
		_state_machine.userdata.bin_5 = 'bin5'
		_state_machine.userdata.bin_4 = 'bin4'
		_state_machine.userdata.bin_3 = 'bin3'
		_state_machine.userdata.bin_2 = 'bin2'
		_state_machine.userdata.bin_6 = 'bin6'
		_state_machine.userdata.camera_ref_frame2 = 'arm2_linear_arm_actuator'
		_state_machine.userdata.rotation = 0
		_state_machine.userdata.offset = 0.1
		_state_machine.userdata.camera_frame_2 = 'logical_camera_drijfstang_frame'
		_state_machine.userdata.camera_frame_3 = 'logical_camera_binR_frame'
		_state_machine.userdata.camera_frame_4 = 'logical_camera_binL_frame'
		_state_machine.userdata.camera_frame_5 = 'logical_camera_pulley_frame'
		_state_machine.userdata.camera_frame_6 = 'logical_camera_pakking_frame'
		_state_machine.userdata.camera_frame_agv1 = 'logical_camera_agvL_frame'
		_state_machine.userdata.camera_frame_agv2 = 'logical_camera_agvR_frame'
		_state_machine.userdata.camera_frame_1 = 'logical_camera_tandwiel_frame'
		_state_machine.userdata.joint_values = []
		_state_machine.userdata.part_type = ''
		_state_machine.userdata.pose = ''
		_state_machine.userdata.joint_names = []
		_state_machine.userdata.move_group_prefix = ''

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]


		with _state_machine:
			# x:30 y:40
			OperatableStateMachine.add('bin1',
										EqualState(),
										transitions={'true': 'DetectCameraPart1', 'false': 'bin2'},
										autonomy={'true': Autonomy.Off, 'false': Autonomy.Off},
										remapping={'value_a': 'bin_location', 'value_b': 'bin_1'})

			# x:556 y:40
			OperatableStateMachine.add('bin3',
										EqualState(),
										transitions={'true': 'DetectCameraPart3', 'false': 'bin4'},
										autonomy={'true': Autonomy.Off, 'false': Autonomy.Off},
										remapping={'value_a': 'bin_location', 'value_b': 'bin_3'})

			# x:912 y:43
			OperatableStateMachine.add('bin4',
										EqualState(),
										transitions={'true': 'DetectCameraPart4', 'false': 'bin5'},
										autonomy={'true': Autonomy.Off, 'false': Autonomy.Off},
										remapping={'value_a': 'bin_location', 'value_b': 'bin_4'})

			# x:1237 y:43
			OperatableStateMachine.add('bin5',
										EqualState(),
										transitions={'true': 'DetectCameraPart5', 'false': 'bin6'},
										autonomy={'true': Autonomy.Off, 'false': Autonomy.Off},
										remapping={'value_a': 'bin_location', 'value_b': 'bin_5'})

			# x:1560 y:41
			OperatableStateMachine.add('bin6',
										EqualState(),
										transitions={'true': 'DetectCameraPart6', 'false': 'failed'},
										autonomy={'true': Autonomy.Off, 'false': Autonomy.Off},
										remapping={'value_a': 'bin_location', 'value_b': 'bin_6'})

			# x:29 y:169
			OperatableStateMachine.add('DetectCameraPart1',
										DetectPartCameraAriacState(time_out=5),
										transitions={'continue': 'ComputePickR2', 'failed': 'failed', 'not_found': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off, 'not_found': Autonomy.Off},
										remapping={'ref_frame': 'camera_ref_frame2', 'camera_topic': 'camera_topic_1', 'camera_frame': 'camera_frame_1', 'part': 'part_type', 'pose': 'pose'})

			# x:291 y:168
			OperatableStateMachine.add('DetectCameraPart2',
										DetectPartCameraAriacState(time_out=5),
										transitions={'continue': 'ComputePickR2', 'failed': 'failed', 'not_found': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off, 'not_found': Autonomy.Off},
										remapping={'ref_frame': 'camera_ref_frame2', 'camera_topic': 'camera_topic_2', 'camera_frame': 'camera_frame_2', 'part': 'part_type', 'pose': 'pose'})

			# x:550 y:167
			OperatableStateMachine.add('DetectCameraPart3',
										DetectPartCameraAriacState(time_out=5),
										transitions={'continue': 'ComputePickR2', 'failed': 'failed', 'not_found': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off, 'not_found': Autonomy.Off},
										remapping={'ref_frame': 'camera_ref_frame2', 'camera_topic': 'camera_topic_3', 'camera_frame': 'camera_frame_3', 'part': 'part_type', 'pose': 'pose'})

			# x:912 y:166
			OperatableStateMachine.add('DetectCameraPart4',
										DetectPartCameraAriacState(time_out=5),
										transitions={'continue': 'ComputePickR1', 'failed': 'failed', 'not_found': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off, 'not_found': Autonomy.Off},
										remapping={'ref_frame': 'camera_ref_frame1', 'camera_topic': 'camera_topic_4', 'camera_frame': 'camera_frame_4', 'part': 'part_type', 'pose': 'pose'})

			# x:1238 y:166
			OperatableStateMachine.add('DetectCameraPart5',
										DetectPartCameraAriacState(time_out=5),
										transitions={'continue': 'ComputePickR1', 'failed': 'failed', 'not_found': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off, 'not_found': Autonomy.Off},
										remapping={'ref_frame': 'camera_ref_frame1', 'camera_topic': 'camera_topic_5', 'camera_frame': 'camera_frame_5', 'part': 'part_type', 'pose': 'pose'})

			# x:1553 y:170
			OperatableStateMachine.add('DetectCameraPart6',
										DetectPartCameraAriacState(time_out=5),
										transitions={'continue': 'ComputePickR1', 'failed': 'failed', 'not_found': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off, 'not_found': Autonomy.Off},
										remapping={'ref_frame': 'camera_ref_frame1', 'camera_topic': 'camera_topic_6', 'camera_frame': 'camera_frame_6', 'part': 'part_type', 'pose': 'pose'})

			# x:301 y:319
			OperatableStateMachine.add('ComputePickR2',
										ComputeGraspAriacState(joint_names=['linear_arm_actuator_joint', 'shoulder_pan_joint', 'shoulder_lift_joint', 'elbow_joint', 'wrist_1_joint', 'wrist_2_joint', 'wrist_3_joint']),
										transitions={'continue': 'ShowJointValues', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'move_group': 'move_group', 'move_group_prefix': 'move_group_prefix', 'tool_link': 'tool_link', 'pose': 'pose', 'offset': 'offset', 'rotation': 'rotation', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:1254 y:317
			OperatableStateMachine.add('ComputePickR1',
										ComputeGraspAriacState(joint_names=['linear_arm_actuator_joint', 'shoulder_pan_joint', 'shoulder_lift_joint', 'elbow_joint', 'wrist_1_joint', 'wrist_2_joint', 'wrist_3_joint']),
										transitions={'continue': 'ShowJointValues', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'move_group': 'move_group', 'move_group_prefix': 'move_group_prefix', 'tool_link': 'tool_link', 'pose': 'pose', 'offset': 'offset', 'rotation': 'rotation', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:761 y:543
			OperatableStateMachine.add('ShowJointValues',
										MessageState(),
										transitions={'continue': 'finished'},
										autonomy={'continue': Autonomy.Off},
										remapping={'message': 'joint_values'})

			# x:293 y:43
			OperatableStateMachine.add('bin2',
										EqualState(),
										transitions={'true': 'DetectCameraPart2', 'false': 'bin3'},
										autonomy={'true': Autonomy.Off, 'false': Autonomy.Off},
										remapping={'value_a': 'bin_location', 'value_b': 'bin_2'})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
