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
from ariac_logistics_flexbe_states.get_products_from_shipment_state import GetProductsFromShipmentState
from ariac_logistics_flexbe_states.get_part_from_products_state import GetPartFromProductsState
from ariac_flexbe_behaviors.transport_part_form_bin_to_agv_state_sm import transport_part_form_bin_to_agv_stateSM
from ariac_flexbe_states.end_assignment_state import EndAssignment
from ariac_logistics_flexbe_states.get_order_state import GetOrderState
# Additional imports can be added inside the following tags
# [MANUAL_IMPORT]

# [/MANUAL_IMPORT]


'''
Created on Wed Apr 22 2020
@author: Gerard Harkema
'''
class transport_part_from_bin_to_arv_2SM(Behavior):
	'''
	Transports a order part from a bin to its desired agv
	'''


	def __init__(self):
		super(transport_part_from_bin_to_arv_2SM, self).__init__()
		self.name = 'transport_part_from_bin_to_arv_2'

		# parameters of this behavior

		# references to used behaviors
		self.add_behavior(transport_part_form_bin_to_agv_stateSM, 'transport_part_form_bin_to_agv_state')

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		# x:1253 y:57, x:671 y:211
		_state_machine = OperatableStateMachine(outcomes=['finished', 'failed'])
		_state_machine.userdata.shipments = []
		_state_machine.userdata.order_id = ''
		_state_machine.userdata.number_of_shipments = 0
		_state_machine.userdata.shipment_index = 0
		_state_machine.userdata.shipment_type = ''
		_state_machine.userdata.agv_id = ''
		_state_machine.userdata.products = []
		_state_machine.userdata.number_of_products = 0
		_state_machine.userdata.product_index = 0
		_state_machine.userdata.part_type = ''
		_state_machine.userdata.part_pose = []

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]


		with _state_machine:
			# x:30 y:40
			OperatableStateMachine.add('StartAssignment',
										StartAssignment(),
										transitions={'continue': 'GetOrder'},
										autonomy={'continue': Autonomy.Off})

			# x:369 y:42
			OperatableStateMachine.add('GetProductsFromShipment',
										GetProductsFromShipmentState(),
										transitions={'continue': 'GetPartFromProducts', 'invalid_index': 'failed'},
										autonomy={'continue': Autonomy.Off, 'invalid_index': Autonomy.Off},
										remapping={'shipments': 'shipments', 'index': 'shipment_index', 'shipment_type': 'shipment_type', 'agv_id': 'agv_id', 'products': 'products', 'number_of_products': 'number_of_products'})

			# x:574 y:43
			OperatableStateMachine.add('GetPartFromProducts',
										GetPartFromProductsState(),
										transitions={'continue': 'transport_part_form_bin_to_agv_state', 'invalid_index': 'failed'},
										autonomy={'continue': Autonomy.Off, 'invalid_index': Autonomy.Off},
										remapping={'products': 'products', 'index': 'product_index', 'type': 'part_type', 'pose': 'part_pose'})

			# x:780 y:44
			OperatableStateMachine.add('transport_part_form_bin_to_agv_state',
										self.use_behavior(transport_part_form_bin_to_agv_stateSM, 'transport_part_form_bin_to_agv_state'),
										transitions={'finished': 'EndAssignment', 'failed': 'failed'},
										autonomy={'finished': Autonomy.Inherit, 'failed': Autonomy.Inherit},
										remapping={'part_type': 'part_type', 'agv_id': 'agv_id', 'pose_on_agv': 'part_pose'})

			# x:1040 y:45
			OperatableStateMachine.add('EndAssignment',
										EndAssignment(),
										transitions={'continue': 'finished'},
										autonomy={'continue': Autonomy.Off})

			# x:181 y:44
			OperatableStateMachine.add('GetOrder',
										GetOrderState(),
										transitions={'continue': 'GetProductsFromShipment'},
										autonomy={'continue': Autonomy.Off},
										remapping={'order_id': 'order_id', 'shipments': 'shipments', 'number_of_shipments': 'number_of_shipments'})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
