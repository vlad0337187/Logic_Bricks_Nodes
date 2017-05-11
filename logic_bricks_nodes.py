'''A collection of logic bricks nodes: sensors, controllers, actuators.
rev.1

Uses:
	# (they must be registered before this modules's classes)
	operators, defined in logic_bricks_operators.py
'''



import bpy
from logic_bricks_colors import *





class LogicBricksSuperclass:
	'''Super class for giving Nodes subclasses
	.poll() method (to enable instantiation).
	'''
	@classmethod
	def poll(cls, ntree):
		return ntree.bl_idname == 'LogicBricksTree'





class Sensor(bpy.types.Node, LogicBricksSuperclass):
	'''Parent class for sensor logic bricks nodes.
	Cannot be placed if subclasses.
	'''
	bl_idname = 'Sensor'
	bl_label = 'Sensor Logic Brick Node'
	bl_icon = 'VISIBLE_IPO_ON'
	
	
	def init(self, context):
		self.outputs.new('SensorToControllerSocket', "out")
		self.use_custom_color = True
		self.color = sensor_color[:-1]
	
	def copy(self, node):
		print("Copying from node ", node)
	
	def free(self):
		print("Removing node ", self, ", Goodbye!")
	
	def draw_label(self):
		return "Sensor node."





class Controller(bpy.types.Node, LogicBricksSuperclass):
	'''Parent class for controller logic bricks nodes.
	'''
	bl_idname = 'Controller'
	bl_label = 'Controller Logic Brick Node'
	bl_icon = 'VISIBLE_IPO_ON'	
	
	
	def init(self, context):
		self.inputs.new('SensorToControllerSocket', "in")
		self.outputs.new('ControllerToActuatorSocket', "out")
		self.use_custom_color = True
		self.color = controller_color[:-1]
	
	def copy(self, node):
		print("Copying from node ", node)
	
	def free(self):
		print("Removing node ", self, ", Goodbye!")
	
	def draw_label(self):
		return "Controller node."





class Actuator(bpy.types.Node, LogicBricksSuperclass):
	'''Parent class for actuator logic bricks nodes.
	'''
	bl_idname = 'Actuator'
	bl_label = 'Actuator Logic Brick Node'
	bl_icon = 'VISIBLE_IPO_ON'	
	
	
	def init(self, context):
		self.inputs.new('ControllerToActuatorSocket', "in")
		self.use_custom_color = True
		self.color = actuator_color[:-1]
	
	def copy(self, node):
		print("Copying from node ", node)
	
	def free(self):
		print("Removing node ", self, ", Goodbye!")
	
	def draw_label(self):
		return "Actuator node."










class ActuatorSensor(Sensor):
	'''Sensor, which tracks some actuator.
	'''
	bl_idname = 'ActuatorSensor'
	bl_label = 'Sensor Logic Brick Node'
	bl_icon = 'VISIBLE_IPO_ON'
	
	def draw_label(self):
		return "Actuator sensor."
	
	bl_width_default = 220.0
	
	# Properties:
	brick_name = bpy.props.StringProperty(default ='Logic brick.')
	positive_pulse = bpy.props.BoolProperty(name="Positive level triggering",
			description="Activale positive level triggering (pulse mode).", default = False)
	negative_pulse = bpy.props.BoolProperty(name="Negative level triggering",
			description="Activale negative level triggering (pulse mode).", default = False)
	shit = bpy.props.StringProperty(default ='Logic brick.')
	
	def draw_buttons(self, context, layout):
		box1 = layout.box()
		box1.prop(self, "brick_name", 'Brick name'),
		box1.prop(self, "positive_pulse")
		box1.prop(self, "negative_pulse")
		box1.prop(self, "shit")
		layout.operator("wm.add_actuator_sensor", icon='FORCE_WIND')










def register_logic_bricks_nodes():
	"""Is launched from logic_bricks.py from register () function.
	"""
	
	#bpy.utils.register_class(Sensor)  # cannot be placed if subclasses
	bpy.utils.register_class(Controller)
	bpy.utils.register_class(Actuator)
	
	bpy.utils.register_class(ActuatorSensor)


def unregister_logic_bricks_nodes():
	"""Is launched from logic_bricks.py from unregister () function.
	"""
	
	#bpy.utils.unregister_class(Sensor)
	bpy.utils.unregister_class(Controller)
	bpy.utils.unregister_class(Actuator)
	
	bpy.utils.unregister_class(ActuatorSensor)