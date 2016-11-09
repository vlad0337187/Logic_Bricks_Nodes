'''Contains tree class for logic nodes.
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
	bpy.utils.register_class(LogicBricksTree)



def unregister_logic_bricks_tree():
	bpy.utils.unregister_class(LogicBricksTree)