'''Defines sockets for logic_node module.
'''

import bpy




class SensorToControllerSocket(bpy.types.NodeSocket):
	'''Socket, that connects sensor to controller.'''
	
	bl_idname = 'SensorToControllerSocket'
	bl_label = 'Sensor to controller socket'  # Label for nice name display

	# Enum items list
	sensor_controller_items = [
		("True", "True", "True logic value"),
		("False", "False", "False logic value"),
		("None", "None", "None value") ]

	sensor_controller_enum_property = bpy.props.EnumProperty(name="Impulse", description="Logic brick True or False impulse, or None.", items=sensor_controller_items, default='None')


	def draw(self, context, layout, node, text):
		'''Draws socket input value.
		'''
		if self.is_output or self.is_linked:
			layout.label(text)
		else:
			layout.prop(self, "Impulse", text=text)

	# Socket color
	def draw_color(self, context, node):
		return (0.1, 0.8, 0.216, 0.5)




class ControllerToActuatorSocket(bpy.types.NodeSocket):
	'''Socket, that connects sensor to actuator.'''
	
	bl_idname = 'ControllerToActuatorSocket'
	bl_label = 'Controller to actuator socket'  # Label for nice name display

	# Enum items list
	controller_actuator_items = [
		('True', "True", "True logic value"),
		('False', "False", "False logic value") ]

	controller_actuator_enum_property = bpy.props.EnumProperty(name="State", description="True\False - activate\not activate actuator.", items=controller_actuator_items, default='False')

	def draw(self, context, layout, node, text):
		'''Draws socket input value.
		'''
		if self.is_output or self.is_linked:
			layout.label(text)
		else:
			layout.prop(self, "Impulse", text=text)

	# Socket color
	def draw_color(self, context, node):
		return (0.8, 0.8, 0.1, 0.5)








def register_logic_bricks_sockets():
	bpy.utils.register_class(SensorToControllerSocket)
	bpy.utils.register_class(ControllerToActuatorSocket)



def unregister_logic_bricks_sockets():
	bpy.utils.unregister_class(SensorToControllerSocket)
	bpy.utils.unregister_class(ControllerToActuatorSocket)