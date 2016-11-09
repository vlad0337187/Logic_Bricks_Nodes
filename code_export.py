'''This script copies all text files into specified folder.
Also it checks: are there extra files in "path_to_text" directory
and shows their names.

Author: Vladislav Naumov. naumovvladislav@list.ru; github.com/vlad1777d; vk.com/naumovvladislav
License: CC-BY. To use this under other license contact author.

Revision: 2
'''
folder_to_copy = './code-logic_bricks'


import bpy
import os  # to get abs. path and list of files in dir ("os.listdir()")




filepath = bpy.data.filepath
filepath = filepath[:filepath.rfind('/') + 1]

path_to_text = os.path.abspath(filepath + folder_to_copy)



names_inner_texts = bpy.data.texts.keys()
extra_texts = []


def check_for_extra_files():
	'''Checks: are files, that are not present in current .blend file,
	present in "path_to_text" folder.
	'''
	global extra_texts
	
	for text in os.listdir(path=path_to_text):
		if text.startswith('.'):
			continue
		elif text in names_inner_texts:
			continue
		else:
			extra_texts.append(text)
	
	if len(extra_texts) > 0:
		print('Found {0} extra text files:'.format(len(extra_texts)), '\n', extra_texts, '\n')


def write_files():
	print('Starting writting files to {0}'.format(path_to_text))
	for key in names_inner_texts:
		obj = bpy.data.texts[key]
		with open( path_to_text + '/{name}'.format(name=key), 'tw' ) as file_to_write:
			file_to_write.write( obj.as_string() )
		print('File {name} was successfully written.'.format(name=key))
	print('\n', 'All files were written.', sep='')
	print('Found {0} extra text files. Their names were specified earlier above.'.format(len(extra_texts)))


print('\n\n\n', 'Script "code export" started.', '\n')
#if __name__ == 'main':  # doesn't work
check_for_extra_files()
write_files()