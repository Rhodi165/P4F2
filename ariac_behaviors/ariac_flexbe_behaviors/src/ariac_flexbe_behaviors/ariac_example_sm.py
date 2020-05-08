#!/usr/bin/env python
# -*- coding: utf-8 -*-
###########################################################
#               WARNING: Generated code!                  #
#              **************************                 #
# Manual changes may get lost if file is generated again. #
# Only code inside the [MANUAL] tags will be kept.        #
###########################################################

from flexbe_core import Behavior, Autonomy, OperatableStateMachine, ConcurrencyContainer, PriorityContainer, Logger
from ariac_flexbe_states.start_assignment_state import StartAssignment
from flexbe_states.wait_state import WaitState
from ariac_flexbe_states.get_object_pose import GetObjectPoseState
from ariac_flexbe_behaviors.notify_shipment_ready_sm import notify_shipment_readySM
from ariac_flexbe_states.srdf_state_to_moveit_ariac_state import SrdfStateToMoveitAriac
from ariac_flexbe_states.moveit_to_joints_dyn_ariac_state import MoveitToJointsDynAriacState
from ariac_flexbe_states.detect_part_camera_ariac_state import DetectPartCameraAriacState
from ariac_flexbe_states.compute_grasp_ariac_state import ComputeGraspAriacState
from ariac_flexbe_states.end_assignment_state import EndAssignment
from ariac_flexbe_states.set_conveyorbelt_power_state import SetConveyorbeltPowerState
# Additional imports can be added inside the following tags
# [MANUAL_IMPORT]

# [/MANUAL_IMPORT]


'''
Created on Thu Apr 16 2020
@author: Gerard Harkema
'''
class ariac_exampleSM(Behavior):
	'''
	Voorbeeld statemachine voor de ariac 2019 opdracht
	'''


	def __init__(self):
		super(ariac_exampleSM, self).__init__()
		self.name = 'ariac_example'

		# parameters of this behavior

		# references to used behaviors
		self.add_behavior(notify_shipment_readySM, 'DeliverShipment')

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		# x:70 y:501, x:515 y:301
		_state_machine = OperatableStateMachine(outcomes=['finished', 'failed'])
		_state_machine.userdata.part_pose = []
		_state_machine.userdata.joint_values = []
		_state_machine.userdata.joint_names = []
		_state_machine.userdata.part = 'gasket_part'
		_state_machine.userdata.offset = 0.1
		_state_machine.userdata.move_group = 'manipulator'
		_state_machine.userdata.move_group_prefix = '/ariac/arm1'
		_state_machine.userdata.config_name_home = 'home'
		_state_machine.userdata.action_topic = '/move_group'
		_state_machine.userdata.robot_name = ''
		_state_machine.userdata.config_name_bin3PreGrasp = 'bin3PreGrasp'
		_state_machine.userdata.config_name_tray1PreDrop = 'tray1PreDrop'
		_state_machine.userdata.camera_ref_frame = 'arm1_linear_arm_actuator'
		_state_machine.userdata.camera_topic = '/ariac/logical_camera_1'
		_state_machine.userdata.camera_frame = 'logical_camera_1_frame'
		_state_machine.userdata.tool_link = 'ee_link'
		_state_machine.userdata.agv_pose = []
		_state_machine.userdata.part_offset = 0.035
		_state_machine.userdata.part_rotation = 0
		_state_machine.userdata.conveyor_belt_power = 100.0

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]


		with _state_machine:
			# x:20 y:140
			OperatableStateMachine.add('StartAssignment',
										StartAssignment(),
										transitions={'continue': 'SetConveyorbeltPower'},
										autonomy={'continue': Autonomy.Off})

			# x:909 y:288
			OperatableStateMachine.add('WachtEven',
										WaitState(wait_time=1),
										transitions={'done': 'MoveR1PreGrasp2'},
										autonomy={'done': Autonomy.Off})

			# x:746 y:427
			OperatableStateMachine.add('GetAgvPose',
										GetObjectPoseState(object_frame='kit_tray_1', ref_frame='arm1_linear_arm_actuator', time_out=5.0),
										transitions={'continue': 'ComuteDorp', 'time_out': 'failed', 'failed': 'ComuteDorp'},
										autonomy={'continue': Autonomy.Off, 'time_out': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'pose': 'agv_pose'})

			# x:373 y:13
			OperatableStateMachine.add('WaitRetry1',
										WaitState(wait_time=5),
										transitions={'done': 'MoveR1Home'},
										autonomy={'done': Autonomy.Off})

			# x:755 y:14
			OperatableStateMachine.add('WaitRetry2',
										WaitState(wait_time=5),
										transitions={'done': 'MoveR1PreGrasp1'},
										autonomy={'done': Autonomy.Off})

			# x:1107 y:222
			OperatableStateMachine.add('WaitRetry3',
										WaitState(wait_time=5),
										transitions={'done': 'MoveR1ToPick1'},
										autonomy={'done': Autonomy.Off})

			# x:1104 y:355
			OperatableStateMachine.add('WaitRetry4',
										WaitState(wait_time=5),
										transitions={'done': 'MoveR1PreGrasp2'},
										autonomy={'done': Autonomy.Off})

			# x:383 y:523
			OperatableStateMachine.add('WaitRetry6',
										WaitState(wait_time=5),
										transitions={'done': 'MoveR1ToDrop'},
										autonomy={'done': Autonomy.Off})

			# x:1104 y:430
			OperatableStateMachine.add('WaitRetry5',
										WaitState(wait_time=5),
										transitions={'done': 'MoveR1PreDrop'},
										autonomy={'done': Autonomy.Off})

			# x:158 y:420
			OperatableStateMachine.add('DeliverShipment',
										self.use_behavior(notify_shipment_readySM, 'DeliverShipment'),
										transitions={'finished': 'EndAssignment', 'failed': 'ComuteDorp'},
										autonomy={'finished': Autonomy.Inherit, 'failed': Autonomy.Inherit})

			# x:733 y:148
			OperatableStateMachine.add('MoveR1PreGrasp1',
										SrdfStateToMoveitAriac(),
										transitions={'reached': 'ComutePick', 'planning_failed': 'WaitRetry2', 'control_failed': 'WaitRetry2', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'config_name_bin3PreGrasp', 'move_group': 'move_group', 'move_group_prefix': 'move_group_prefix', 'action_topic': 'action_topic', 'robot_name': 'robot_name', 'config_name_out': 'config_name_out', 'move_group_out': 'move_group_out', 'robot_name_out': 'robot_name_out', 'action_topic_out': 'action_topic_out', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:910 y:355
			OperatableStateMachine.add('MoveR1PreGrasp2',
										SrdfStateToMoveitAriac(),
										transitions={'reached': 'MoveR1PreDrop', 'planning_failed': 'WaitRetry4', 'control_failed': 'WaitRetry4', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'config_name_bin3PreGrasp', 'move_group': 'move_group', 'move_group_prefix': 'move_group_prefix', 'action_topic': 'action_topic', 'robot_name': 'robot_name', 'config_name_out': 'config_name_out', 'move_group_out': 'move_group_out', 'robot_name_out': 'robot_name_out', 'action_topic_out': 'action_topic_out', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:913 y:428
			OperatableStateMachine.add('MoveR1PreDrop',
										SrdfStateToMoveitAriac(),
										transitions={'reached': 'GetAgvPose', 'planning_failed': 'WaitRetry5', 'control_failed': 'WaitRetry5', 'param_error': 'ComuteDorp'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'config_name_tray1PreDrop', 'move_group': 'move_group', 'move_group_prefix': 'move_group_prefix', 'action_topic': 'action_topic', 'robot_name': 'robot_name', 'config_name_out': 'config_name_out', 'move_group_out': 'move_group_out', 'robot_name_out': 'robot_name_out', 'action_topic_out': 'action_topic_out', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:908 y:220
			OperatableStateMachine.add('MoveR1ToPick1',
										MoveitToJointsDynAriacState(),
										transitions={'reached': 'WachtEven', 'planning_failed': 'WaitRetry3', 'control_failed': 'WaitRetry3'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off},
										remapping={'move_group_prefix': 'move_group_prefix', 'move_group': 'move_group', 'action_topic': 'action_topic', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:349 y:422
			OperatableStateMachine.add('MoveR1ToDrop',
										MoveitToJointsDynAriacState(),
										transitions={'reached': 'DeliverShipment', 'planning_failed': 'WaitRetry6', 'control_failed': 'WaitRetry6'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off},
										remapping={'move_group_prefix': 'move_group_prefix', 'move_group': 'move_group', 'action_topic': 'action_topic', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:526 y:146
			OperatableStateMachine.add('DetectCameraPart',
										DetectPartCameraAriacState(time_out=5.0),
										transitions={'continue': 'MoveR1PreGrasp1', 'failed': 'failed', 'not_found': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off, 'not_found': Autonomy.Off},
										remapping={'ref_frame': 'camera_ref_frame', 'camera_topic': 'camera_topic', 'camera_frame': 'camera_frame', 'part': 'part', 'pose': 'pose'})

			# x:908 y:148
			OperatableStateMachine.add('ComutePick',
										ComputeGraspAriacState(joint_names=['linear_arm_actuator_joint', 'shoulder_pan_joint', 'shoulder_lift_joint', 'elbow_joint', 'wrist_1_joint', 'wrist_2_joint', 'wrist_3_joint']),
										transitions={'continue': 'MoveR1ToPick1', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'move_group': 'move_group', 'move_group_prefix': 'move_group_prefix', 'tool_link': 'tool_link', 'pose': 'pose', 'offset': 'part_offset', 'rotation': 'part_rotation', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:539 y:424
			OperatableStateMachine.add('ComuteDorp',
										ComputeGraspAriacState(joint_names=['linear_arm_actuator_joint', 'shoulder_pan_joint', 'shoulder_lift_joint', 'elbow_joint', 'wrist_1_joint', 'wrist_2_joint', 'wrist_3_joint']),
										transitions={'continue': 'MoveR1ToDrop', 'failed': 'MoveR1ToDrop'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'move_group': 'move_group', 'move_group_prefix': 'move_group_prefix', 'tool_link': 'tool_link', 'pose': 'agv_pose', 'offset': 'part_offset', 'rotation': 'part_rotation', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:353 y:143
			OperatableStateMachine.add('MoveR1Home',
										SrdfStateToMoveitAriac(),
										transitions={'reached': 'DetectCameraPart', 'planning_failed': 'WaitRetry1', 'control_failed': 'WaitRetry1', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'config_name_home', 'move_group': 'move_group', 'move_group_prefix': 'move_group_prefix', 'action_topic': 'action_topic', 'robot_name': 'robot_name', 'config_name_out': 'config_name_out', 'move_group_out': 'move_group_out', 'robot_name_out': 'robot_name_out', 'action_topic_out': 'action_topic_out', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:28 y:422
			OperatableStateMachine.add('EndAssignment',
										EndAssignment(),
										transitions={'continue': 'finished'},
										autonomy={'continue': Autonomy.Off})

			# x:165 y:144
			OperatableStateMachine.add('SetConveyorbeltPower',
										SetConveyorbeltPowerState(),
										transitions={'continue': 'MoveR1Home', 'fail': 'failed'},
										autonomy={'continue': Autonomy.Off, 'fail': Autonomy.Off},
										remapping={'power': 'conveyor_belt_power'})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
