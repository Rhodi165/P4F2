#!/usr/bin/env python
# -*- coding: utf-8 -*-
###########################################################
#               WARNING: Generated code!                  #
#              **************************                 #
# Manual changes may get lost if file is generated again. #
# Only code inside the [MANUAL] tags will be kept.        #
###########################################################

from flexbe_core import Behavior, Autonomy, OperatableStateMachine, ConcurrencyContainer, PriorityContainer, Logger
from ariac_logistics_flexbe_states.get_material_locations import GetMaterialLocationsState
from ariac_flexbe_states.message_state import MessageState
from ariac_support_flexbe_states.get_item_from_list_state import GetItemFromListState
from ariac_flexbe_behaviors.select_agv_sm import SelectagvSM
# Additional imports can be added inside the following tags
# [MANUAL_IMPORT]

# [/MANUAL_IMPORT]


'''
Created on Wed Apr 22 2020
@author: Gerard Harkema
'''
class transport_part_form_bin_to_agv_stateSM(Behavior):
	'''
	transports part from it's bin to the selected agv
	'''


	def __init__(self):
		super(transport_part_form_bin_to_agv_stateSM, self).__init__()
		self.name = 'transport_part_form_bin_to_agv_state'

		# parameters of this behavior

		# references to used behaviors
		self.add_behavior(SelectagvSM, 'Select agv')

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		# x:1739 y:605, x:506 y:446
		_state_machine = OperatableStateMachine(outcomes=['finished', 'failed'], input_keys=['part_type', 'agv_id', 'pose_on_agv'])
		_state_machine.userdata.part_type = ''
		_state_machine.userdata.agv_id = ''
		_state_machine.userdata.pose_on_agv = []
		_state_machine.userdata.material_locations = []
		_state_machine.userdata.bin_location = ''
		_state_machine.userdata.zero_value = 0

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]


		with _state_machine:
			# x:57 y:121
			OperatableStateMachine.add('GetPartLocation',
										GetMaterialLocationsState(),
										transitions={'continue': 'GetBinLocation'},
										autonomy={'continue': Autonomy.Off},
										remapping={'part': 'part_type', 'material_locations': 'material_locations'})

			# x:1083 y:110
			OperatableStateMachine.add('MoseMessage',
										MessageState(),
										transitions={'continue': 'Select agv'},
										autonomy={'continue': Autonomy.Off},
										remapping={'message': 'pose_on_agv'})

			# x:690 y:117
			OperatableStateMachine.add('PartTypeMessage',
										MessageState(),
										transitions={'continue': 'BinLocation'},
										autonomy={'continue': Autonomy.Off},
										remapping={'message': 'part_type'})

			# x:288 y:118
			OperatableStateMachine.add('GetBinLocation',
										GetItemFromListState(),
										transitions={'done': 'AgvIdMessage', 'invalid_index': 'failed'},
										autonomy={'done': Autonomy.Off, 'invalid_index': Autonomy.Off},
										remapping={'list': 'material_locations', 'index': 'zero_value', 'item': 'bin_location'})

			# x:525 y:114
			OperatableStateMachine.add('AgvIdMessage',
										MessageState(),
										transitions={'continue': 'PartTypeMessage'},
										autonomy={'continue': Autonomy.Off},
										remapping={'message': 'agv_id'})

			# x:874 y:122
			OperatableStateMachine.add('BinLocation',
										MessageState(),
										transitions={'continue': 'MoseMessage'},
										autonomy={'continue': Autonomy.Off},
										remapping={'message': 'material_locations'})

			# x:1286 y:109
			OperatableStateMachine.add('Select agv',
										self.use_behavior(SelectagvSM, 'Select agv'),
										transitions={'finished': 'finished', 'failed': 'failed'},
										autonomy={'finished': Autonomy.Inherit, 'failed': Autonomy.Inherit},
										remapping={'agv_id': 'agv_id', 'bin_location': 'bin_location', 'pose_on_agv': 'pose_on_agv', 'bin_location': 'bin_location'})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
