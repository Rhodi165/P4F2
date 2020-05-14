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
from ariac_logistics_flexbe_states.get_order_state import GetOrderState
from ariac_logistics_flexbe_states.get_products_from_shipment_state import GetProductsFromShipmentState
from ariac_logistics_flexbe_states.get_part_from_products_state import GetPartFromProductsState
from ariac_flexbe_behaviors.transport_part_form_bin_to_agv_state_sm import transport_part_form_bin_to_agv_stateSM
from ariac_support_flexbe_states.add_numeric_state import AddNumericState
from ariac_support_flexbe_states.equal_state import EqualState
from ariac_support_flexbe_states.replace_state import ReplaceState
# Additional imports can be added inside the following tags
# [MANUAL_IMPORT]

# [/MANUAL_IMPORT]


'''
Created on Wed May 13 2020
@author: Lein en Timon
'''
class testSM(Behavior):
	'''
	programma versie 1
	'''


	def __init__(self):
		super(testSM, self).__init__()
		self.name = 'test'

		# parameters of this behavior

		# references to used behaviors
		self.add_behavior(transport_part_form_bin_to_agv_stateSM, 'transport_part_form_bin_to_agv_state')

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		# x:1715 y:320, x:65 y:327
		_state_machine = OperatableStateMachine(outcomes=['finished', 'failed'])
		_state_machine.userdata.order_id = ''
		_state_machine.userdata.shipments = []
		_state_machine.userdata.number_of_shipments = 0
		_state_machine.userdata.shipment_index = 0
		_state_machine.userdata.shipment_type = ''
		_state_machine.userdata.agv_id = ''
		_state_machine.userdata.products = []
		_state_machine.userdata.number_of_products = 0
		_state_machine.userdata.product_index = 0
		_state_machine.userdata.part_type = ''
		_state_machine.userdata.part_pose = []
		_state_machine.userdata.one_value = 1
		_state_machine.userdata.zero_value = 0

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]


		with _state_machine:
			# x:53 y:34
			OperatableStateMachine.add('StartAssignment',
										StartAssignment(),
										transitions={'continue': 'GetOrder'},
										autonomy={'continue': Autonomy.Off})

			# x:241 y:39
			OperatableStateMachine.add('GetOrder',
										GetOrderState(),
										transitions={'continue': 'GetProductsFromShipments'},
										autonomy={'continue': Autonomy.Off},
										remapping={'order_id': 'order_id', 'shipments': 'shipments', 'number_of_shipments': 'number_of_shipments'})

			# x:479 y:45
			OperatableStateMachine.add('GetProductsFromShipments',
										GetProductsFromShipmentState(),
										transitions={'continue': 'GetPartFromProduct', 'invalid_index': 'failed'},
										autonomy={'continue': Autonomy.Off, 'invalid_index': Autonomy.Off},
										remapping={'shipments': 'shipments', 'index': 'shipment_index', 'shipment_type': 'shipment_type', 'agv_id': 'agv_id', 'products': 'products', 'number_of_products': 'number_of_products'})

			# x:746 y:49
			OperatableStateMachine.add('GetPartFromProduct',
										GetPartFromProductsState(),
										transitions={'continue': 'transport_part_form_bin_to_agv_state', 'invalid_index': 'failed'},
										autonomy={'continue': Autonomy.Off, 'invalid_index': Autonomy.Off},
										remapping={'products': 'products', 'index': 'product_index', 'type': 'part_type', 'pose': 'part_pose'})

			# x:974 y:46
			OperatableStateMachine.add('transport_part_form_bin_to_agv_state',
										self.use_behavior(transport_part_form_bin_to_agv_stateSM, 'transport_part_form_bin_to_agv_state'),
										transitions={'finished': 'IncrementProductIndex', 'failed': 'failed'},
										autonomy={'finished': Autonomy.Inherit, 'failed': Autonomy.Inherit},
										remapping={'part_type': 'part_type', 'agv_id': 'agv_id', 'pose_on_agv': 'part_pose'})

			# x:1315 y:91
			OperatableStateMachine.add('IncrementProductIndex',
										AddNumericState(),
										transitions={'done': 'EindeProducts'},
										autonomy={'done': Autonomy.Off},
										remapping={'value_a': 'product_index', 'value_b': 'one_value', 'result': 'product_index'})

			# x:1069 y:198
			OperatableStateMachine.add('EindeProducts',
										EqualState(),
										transitions={'true': 'ResetProductIndex', 'false': 'GetPartFromProduct'},
										autonomy={'true': Autonomy.Off, 'false': Autonomy.Off},
										remapping={'value_a': 'product_index', 'value_b': 'number_of_products'})

			# x:1311 y:452
			OperatableStateMachine.add('IncrementShipmentIndex',
										AddNumericState(),
										transitions={'done': 'EindeShipments'},
										autonomy={'done': Autonomy.Off},
										remapping={'value_a': 'shipment_index', 'value_b': 'one_value', 'result': 'shipment_index'})

			# x:1064 y:505
			OperatableStateMachine.add('EindeShipments',
										EqualState(),
										transitions={'true': 'ResetShipments', 'false': 'GetProductsFromShipments'},
										autonomy={'true': Autonomy.Off, 'false': Autonomy.Off},
										remapping={'value_a': 'shipment_index', 'value_b': 'number_of_shipments'})

			# x:1194 y:316
			OperatableStateMachine.add('ResetProductIndex',
										ReplaceState(),
										transitions={'done': 'IncrementShipmentIndex'},
										autonomy={'done': Autonomy.Off},
										remapping={'value': 'zero_value', 'result': 'product_index'})

			# x:1213 y:622
			OperatableStateMachine.add('ResetShipments',
										ReplaceState(),
										transitions={'done': 'finished'},
										autonomy={'done': Autonomy.Off},
										remapping={'value': 'zero_value', 'result': 'product_index'})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
