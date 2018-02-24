f="HW1-Test-"
for (( i=0; i<=56; i++))
	do
        wget http://boston.lti.cs.cmu.edu/classes/11-642/HW/HTS/tests/$f$i.teIn 
        wget http://boston.lti.cs.cmu.edu/classes/11-642/HW/HTS/tests/$f$i.qry
        wget http://boston.lti.cs.cmu.edu/classes/11-642/HW/HTS/tests/$f$i.param
	done
