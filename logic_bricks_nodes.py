'''A collection of logic bricks nodes: sensors, controllers, actuators.
'''

import bpy




class LogicBricksPollSuperclass:
	'''Super class for giving Nodes subclasses
	.poll() method (to enable instantiation).
	'''
    @classmethod
    def poll(cls, ntree):
        return ntree.bl_idname == 'LogicBricksTree'