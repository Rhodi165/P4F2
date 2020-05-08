#!/usr/bin/env python
# -*- coding: utf-8 -*-
###########################################################
#               WARNING: Generated code!                  #
#              **************************                 #
# Manual changes may get lost if file is generated again. #
# Only code inside the [MANUAL] tags will be kept.        #
###########################################################

from flexbe_core import Behavior, Autonomy, OperatableStateMachine, ConcurrencyContainer, PriorityContainer, Logger
from ariac_flexbe_states.detect_first_part_camera_ariac_state import DetectFirstPartCameraAriacState
from ariac_flexbe_states.message_state import MessageState
from ariac_flexbe_states.start_assignment_state import StartAssignment
from ariac_flexbe_states.end_assignment_state import EndAssignment
# Additional imports can be added inside the following tags
# [MANUAL_IMPORT]

# [/MANUAL_IMPORT]


'''
Created on Mon Apr 27 2020
@author: Gerard Harkema
'''
class detect_first_part_camera_exampleSM(Behavior):
	'''
	Example to detect a part form a partlist biy the camera
	'''


	def __init__(self):
		super(detect_first_part_camera_exampleSM, self).__init__()
		self.name = 'detect_first_part_camera_example'

		# parameters of this behavior

		# references to used behaviors

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		part_list = ['gasket_part', 'piston_rod_part', 'gear_part', ' pulley_part', 'disk_part']
		# x:842 y:52, x:158 y:179
		_state_machine = OperatableStateMachine(outcomes=['finished', 'failed'])
		_state_machine.userdata.camera_ref_frame = "arm1_linear_arm_actuator"
		_state_machine.userdata.camera_topic = "/ariac/logical_camera_1"
		_state_machine.userdata.camera_frame = "logical_camera_1_frame"
		_state_machine.userdata.pose = []
		_state_machine.userdata.part = ''

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]


		with _state_machine:
			# x:33 y:38
			OperatableStateMachine.add('StaerAssignment',
										StartAssignment(),
										transitions={'continue': 'DetectFirstPartCamera'},
										autonomy={'continue': Autonomy.Off})

			# x:379 y:40
			OperatableStateMachine.add('PartMessage',
										MessageState(),
										transitions={'continue': 'PoseMessage'},
										autonomy={'continue': Autonomy.Off},
										remapping={'message': 'part'})

			# x:523 y:40
			OperatableStateMachine.add('PoseMessage',
										MessageState(),
										transitions={'continue': 'EndAssignment'},
										autonomy={'continue': Autonomy.Off},
										remapping={'message': 'pose'})

			# x:666 y:37
			OperatableStateMachine.add('EndAssignment',
										EndAssignment(),
										transitions={'continue': 'finished'},
										autonomy={'continue': Autonomy.Off})

			# x:170 y:40
			OperatableStateMachine.add('DetectFirstPartCamera',
										DetectFirstPartCameraAriacState(part_list=part_list, time_out=0.5),
										transitions={'continue': 'PartMessage', 'failed': 'failed', 'not_found': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off, 'not_found': Autonomy.Off},
										remapping={'ref_frame': 'camera_ref_frame', 'camera_topic': 'camera_topic', 'camera_frame': 'camera_frame', 'part': 'part', 'pose': 'pose'})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
