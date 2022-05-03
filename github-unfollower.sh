#! /bin/bash
# init

main () {
	# Run the program
	python main.py
	echo "--------------"
	pause 'Press any key to exit...'
	
}

function pause(){
   read -p "$*"
}


# Start the program
main