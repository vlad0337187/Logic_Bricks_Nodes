'''A collection of logic bricks nodes: sensors, controllers, actuators.
'''


import bpy





class LogicBricksSuperclass:
	'''Super class for giving Nodes subclasses
	.poll() method (to enable instantiation).
	'''
	@classmethod
	def poll(cls, ntree):
		return ntree.bl_idname == 'LogicBricksTree'





class Sensor(bpy.types.Node, LogicBricksSuperclass):
	'''Class for sensor logic bricks nodes.
	'''
	bl_idname = 'Sensor'
	bl_label = 'Sensor Logic Brick Node'
	bl_icon = 'VISIBLE_IPO_ON'
	
	
	def init(self, context):
		self.outputs.new('SensorToControllerSocket', "out")
	
	def copy(self, node):
		print("Copying from node ", node)
	
	def free(self):
		print("Removing node ", self, ", Goodbye!")
	
	def draw_label(self):
		return "Sensor node."




class Controller(bpy.types.Node, LogicBricksSuperclass):
	'''Class for controller logic bricks nodes.
	'''
	bl_idname = 'Controller'
	bl_label = 'Controller Logic Brick Node'
	bl_icon = 'VISIBLE_IPO_ON'	
	
	
	def init(self, context):
		self.inputs.new('SensorToControllerSocket', "in")
		self.outputs.new('ControllerToActuatorSocket', "out")
		self.use_custom_color = True
		self.color = (1.0, 0.4, 0.216)
	
	def copy(self, node):
		print("Copying from node ", node)
	
	def free(self):
		print("Removing node ", self, ", Goodbye!")
	
	def draw_label(self):
		return "Controller node."









def register_logic_bricks_nodes():
	bpy.utils.register_class(Sensor)
	bpy.utils.register_class(Controller)


def unregister_logic_bricks_nodes():
	bpy.utils.unregister_class(Sensor)
	bpy.utils.unregister_class(Controller)