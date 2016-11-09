#! /bin/bash

cd '/home/vlad/Programs/My_projects/Logic_Bricks/code-logic_bricks'
hg status
hg commit
hg bookmark -r default master
hg push Logic_Bricks_Nodes
