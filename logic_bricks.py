'''This module provides Node wrapper over general logic bricks.
rev.1

Tasks:
	-make ability to change type of logic brick (first value).
'''


import bpy

from logic_bricks_tree import *
from logic_bricks_sockets import *
from logic_bricks_operators import *
from logic_bricks_nodes import *
from logic_bricks_categories import *




def register():
	register_logic_bricks_tree ()
	register_logic_bricks_sockets ()
	register_logic_bricks_operators ()
	register_logic_bricks_nodes ()
	
	register_logic_bricks_categories ()


def unregister():
	unregister_logic_bricks_categories ()
	
	unregister_logic_bricks_tree ()
	unregister_logic_bricks_sockets ()
	unregister_logic_bricks_nodes ()
	unregister_logic_bricks_operators ()


if __name__ == "__main__":
	try:
		bpy.activated
	except AttributeError:
		register()
		bpy.activated = True
	else:
		unregister()
		del bpy.activated