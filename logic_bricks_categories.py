'''Contains categories of logic bricks nodes.
'''


import nodeitems_utils
from nodeitems_utils import NodeCategory, NodeItem




class LogicBricksCategory(NodeCategory):
	'''Class for our categories.
	'''
	@classmethod
	def poll(cls, context):
		return context.space_data.tree_type == 'LogicBricksTree'




logic_bricks_nodes_categories = [
	# identifier, label, items list
	LogicBricksCategory('Sensors', "Sensors:", items = [
	NodeItem("Sensor") ]),
	LogicBricksCategory('Controllers', "Controllers:", items = [
	NodeItem("Controller")]),
	LogicBricksCategory('Actuators', "Actuators:", items = [])
	]








def register_logic_bricks_categories():
	nodeitems_utils.register_node_categories("Logic_Bricks_Nodes",
	logic_bricks_nodes_categories)


def unregister_logic_bricks_categories():
	nodeitems_utils.register_node_categories("Logic_Bricks_Nodes",
	logic_bricks_nodes_categories)