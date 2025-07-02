from optparse import OptionParser

#Getting the options you define when calling the script.
usage="usage: checkvals.py -i val" 
parser=OptionParser()
parser.add_option("-i", "--val-1", type="float", help="value1", dest='val_1')
(opts, args) = parser.parse_args()

if float(opts.val_1) < 1.:
	print(1)
if float(opts.val_1) > 1.:
	print(2)
