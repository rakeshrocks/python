snap_tbl = {
	'inode':100,
	'i_gen':12340,
	'parent_inode':64,
	'pgen':345,
}



snap_tbl['inode'] = 500

del snap_tbl['pgen']

for token in snap_tbl:
    print(token)

for name, value in snap_tbl.items():  # Keys & values
    print('{} is {} '.format(name, value))
