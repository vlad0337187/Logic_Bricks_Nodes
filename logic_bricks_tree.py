'''Contains tree class for logic nodes.
rev.1
'''


import bpy





class LogicBricksTree(bpy.types.NodeTree):
	'''Logic bricks nodes three.'''
	
	bl_idname = 'LogicBricksTree'
	bl_label = 'Logic Bricks Nodes'  # Label for nice name display
	bl_icon = 'GAME'
	
	
	@classmethod
	def poll(cls, context):
		# typical shader node test for compatible render engine setting
		#return bpy.context.scene.render.engine == 'BLENDER_GAME'
		return True





def register_logic_bricks_tree():
	"""Is launched from logic_bricks.py from register () function.
	"""
	bpy.utils.register_class(LogicBricksTree)



def unregister_logic_bricks_tree():
	"""Is launched from logic_bricks.py from register () function.
	"""
	bpy.utils.unregister_class(LogicBricksTree)