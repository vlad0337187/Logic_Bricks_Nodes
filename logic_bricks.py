'''This module provides Node wrapper over general logic bricks.
'''

import bpy

sensor_color = (0.1, 0.8, 0.216)
controller_color = (0.8, 0.8, 0.1)
actuator_color = (0.9, 0.1, 0.1)

from logic_bricks_tree import *
from logic_bricks_sockets import *
from logic_bricks_nodes import *
from logic_bricks_categories import *









def register():
	register_logic_bricks_tree()
	register_logic_bricks_sockets()
	register_logic_bricks_nodes()
	
	register_logic_bricks_categories()


def unregister():
	unregister_logic_bricks_categories()
	
	unregister_logic_bricks_tree()
	unregister_logic_bricks_sockets()
	unregister_logic_bricks_nodes()


if __name__ == "__main__":
	register()