import sys
from toplib.models import topsis


def main():
	sysarglist = sys.argv
	sysarglist.pop(0)
	assert len(sysarglist) == 3, "Insufficient number of arguments provided"

	filename = sys.argv[1]
	assert filename, "Filename must be provided"
	topsis(sysarglist)
