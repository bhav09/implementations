#file to extract zip file

# dependency
from zipfile import ZipFile

# opening the zip file in READ mode
with ZipFile('Object Detection files/Object_Detection_Files.zip', 'r') as zip:
	# printing all the contents of the zip file
	zip.printdir()

	# extracting all the files
	print('Extracting all the files..')
	zip.extractall(path='Object Detection files')
	print('Done!')
