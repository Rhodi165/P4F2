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
from ariac_flexbe_states.end_assignment_state import EndAssignment
from ariac_flexbe_states.message_state import MessageState
from ariac_logistics_flexbe_states.get_order_state import GetOrderState
from ariac_flexbe_behaviors.get_shipments_sm import get_shipmentsSM
# Additional imports can be added inside the following tags
# [MANUAL_IMPORT]

# [/MANUAL_IMPORT]


'''
Created on Sun Apr 19 2020
@author: Gerard Harkema
'''
class get_orderSM(Behavior):
	'''
	Tests the starting and stopping of the assignment
	'''


	def __init__(self):
		super(get_orderSM, self).__init__()
		self.name = 'get_order'

		# parameters of this behavior

		# references to used behaviors
		self.add_behavior(get_shipmentsSM, 'get_shipments')

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		# x:1132 y:54, x:687 y:211
		_state_machine = OperatableStateMachine(outcomes=['finished', 'fail'])
		_state_machine.userdata.StartText = 'Opdracht gestart'
		_state_machine.userdata.StopText = 'Opdracht gestopt'
		_state_machine.userdata.Shipments = []
		_state_machine.userdata.part = 'gear_part'
		_state_machine.userdata.material_locations = []
		_state_machine.userdata.NumberOfShipments = 0
		_state_machine.userdata.OrderId = ''
		_state_machine.userdata.Products = []
		_state_machine.userdata.NumberOfProducts = 0

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]


		with _state_machine:
			# x:30 y:40
			OperatableStateMachine.add('StartAssignment',
										StartAssignment(),
										transitions={'continue': 'StartMessage'},
										autonomy={'continue': Autonomy.Off})

			# x:803 y:41
			OperatableStateMachine.add('EndAssigment',
										EndAssignment(),
										transitions={'continue': 'StopMessage'},
										autonomy={'continue': Autonomy.Off})

			# x:158 y:41
			OperatableStateMachine.add('StartMessage',
										MessageState(),
										transitions={'continue': 'GetOrder'},
										autonomy={'continue': Autonomy.Off},
										remapping={'message': 'StartText'})

			# x:963 y:44
			OperatableStateMachine.add('StopMessage',
										MessageState(),
										transitions={'continue': 'finished'},
										autonomy={'continue': Autonomy.Off},
										remapping={'message': 'StopText'})

			# x:286 y:41
			OperatableStateMachine.add('GetOrder',
										GetOrderState(),
										transitions={'continue': 'OrderIdMessage'},
										autonomy={'continue': Autonomy.Off},
										remapping={'order_id': 'OrderId', 'shipments': 'Shipments', 'number_of_shipments': 'NumberOfShipments'})

			# x:466 y:41
			OperatableStateMachine.add('OrderIdMessage',
										MessageState(),
										transitions={'continue': 'get_shipments'},
										autonomy={'continue': Autonomy.Off},
										remapping={'message': 'OrderId'})

			# x:614 y:40
			OperatableStateMachine.add('get_shipments',
										self.use_behavior(get_shipmentsSM, 'get_shipments'),
										transitions={'finished': 'EndAssigment', 'fail': 'fail'},
										autonomy={'finished': Autonomy.Inherit, 'fail': Autonomy.Inherit},
										remapping={'Shipments': 'Shipments', 'NumberOfShipments': 'NumberOfShipments'})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
