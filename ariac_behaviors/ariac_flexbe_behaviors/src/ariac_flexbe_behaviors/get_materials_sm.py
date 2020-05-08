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
from ariac_flexbe_states.message_state import MessageState
from ariac_flexbe_states.end_assignment_state import EndAssignment
from ariac_logistics_flexbe_states.get_material_locations import GetMaterialLocationsState
# Additional imports can be added inside the following tags
# [MANUAL_IMPORT]

# [/MANUAL_IMPORT]


'''
Created on Thu Apr 23 2020
@author: Gerard Harkema
'''
class get_materialsSM(Behavior):
	'''
	Demo to get materail locations of a specific part
	'''


	def __init__(self):
		super(get_materialsSM, self).__init__()
		self.name = 'get_materials'

		# parameters of this behavior

		# references to used behaviors

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		# x:705 y:41
		_state_machine = OperatableStateMachine(outcomes=['finished'])
		_state_machine.userdata.MaterialLocations = []
		_state_machine.userdata.Part = 'piston_rod_part'

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]


		with _state_machine:
			# x:34 y:25
			OperatableStateMachine.add('StartAssignment',
										StartAssignment(),
										transitions={'continue': 'GetMaterialsLocations'},
										autonomy={'continue': Autonomy.Off})

			# x:362 y:28
			OperatableStateMachine.add('MaterialsLocationMessage',
										MessageState(),
										transitions={'continue': 'EndAssignment'},
										autonomy={'continue': Autonomy.Off},
										remapping={'message': 'MaterialLocations'})

			# x:541 y:29
			OperatableStateMachine.add('EndAssignment',
										EndAssignment(),
										transitions={'continue': 'finished'},
										autonomy={'continue': Autonomy.Off})

			# x:176 y:26
			OperatableStateMachine.add('GetMaterialsLocations',
										GetMaterialLocationsState(),
										transitions={'continue': 'MaterialsLocationMessage'},
										autonomy={'continue': Autonomy.Off},
										remapping={'part': 'Part', 'material_locations': 'MaterialLocations'})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
