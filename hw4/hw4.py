# For python 2.7 because 3.8 don't understand TransactionSet()
# Also because of security problems i couldn't read the TAG of the packages I downloaded online
# so I created my own RPM package and applied some release TAG (see setup.py).
import rpm, sys ,os

#Task:There is some rpm-file. Create program that outputs header field rpm.RPMTAG_RELEASE of this file
#How it works: it reads header of the file /home/usr/some_file.rpm and print field like this: 12
#Command: python hw4.py /home/usr/some_file.rpm

rpm_file = os.open(sys.argv[1], os.O_RDONLY)
ts = rpm.TransactionSet()
package = ts.hdrFromFdno(rpm_file)
print("RELEASE...:", package[rpm.RPMTAG_RELEASE])