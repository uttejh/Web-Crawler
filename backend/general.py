#! /usr/bin/python
import os

# Creates seperate folders for each website we crawl
def create_project_dir(directory):
	if not os.path.exists(directory):
		print('Creating Directory:' + directory)
		os.makedirs(directory)


# Creates Queue and Crawled files for urls
def create_data_files(project_name, base_url):
	queue = project_name + '/queue.txt'
	crawled = project_name + '/crawled.txt'

	if not os.path.isfile(queue):
		write_file(queue, base_url)
	if not os.path.isfile(crawled):
		write_file(crawled,'')

# creates a file
def write_file(path, data):
	f = open(path,'w')
	f.write(data)
	f.close()

# Appends links to a file
def append_to_file(path, data):
	with open(path, 'a') as file:
		file.write(data + '\n')

# Deletes links from file
def delete_file_contents(path):
	with open(path, 'w'):
		pass

# Reads a file and converts file to a set
def file_to_set(file_name):
	results = set()
	with open(file_name, 'rt') as f:
		for line in f:
			results.add(line.replace('\n',''))
	return results

# Appends a set of links to the file
def set_to_file(links, file):
	delete_file_contents(file)
	for link in sorted(links):
		append_to_file(file, link)


