'''This module provides Node wrapper over general logic bricks.
'''

import bpy
from logic_bricks_tree import *
from logic_bricks_sockets import *






def register():
	register_logic_bricks_tree()
	register_logic_bricks_sockets()


def unregister():
	unregister_logic_bricks_tree()
	unregister_logic_bricks_sockets()


if __name__ == "__main__":
	register()