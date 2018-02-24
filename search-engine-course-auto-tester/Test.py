import os
s = 'javac -cp ".:lucene-6.6.0/*" -g src/*.java -d bin/'
os.system(s)
test = "HW1-Test"
for i in range(0, 30):
    testcase = i
    filetowrite = ['test.param', "my{1}-{0}.teIn".format(testcase, test)]
    with open(filetowrite[0], 'w') as f:
        f.write("indexPath=[indexpath]\n")
        f.write(
            "queryFilePath=[yourcodedir]/testcase/{1}-{0}.qry\n".format(testcase, test))
        f.write(
            "trecEvalOutputPath=[yourcodedir]/my{1}-{0}.teIn\n".format(testcase, test))
        # f.write("trecEvalOutputLength=100\n")
        with open("testcase/{1}-{0}.param".format(testcase, test)) as f2:
            r = f2.readlines()
            flag = 0
            for i in r:
                if "trecEvalOutputLength" in i:
                    f.write(i)
                    flag = 1
                else:
                    if flag == 1:
                        f.write(i)
    os.chdir("[yourcodedir]/bin")
    print(os.getcwd())
    code2 = 'java -classpath ".:[yourcodedir]/lucene-6.6.0/*" QryEval [yourcodedir]/test.param'
    os.system(code2)
    os.chdir("[yourcodedir]")
    wrong = False
    with open("testcase/{1}-{0}.teIn".format(testcase, test)) as f1:
        r1 = f1.readlines()
        with open("my{1}-{0}.teIn".format(testcase, test)) as f2:
            r2 = f2.readlines()
            for i in range(len(r1)):
                id1 = r1[i].split(" ")[2]
                id2 = r2[i].split(" ")[2]
                if id1 != id2:
                    print("WRONG in TESTCASE {0} in line {1}".format(
                        testcase, i))
                    wrong = True
                    os.system(
                        "cp " + "testcase/{1}-{0}.teIn".format(testcase, test) + " . ")
                    break
    if wrong == False:
        print("RIGHT in testcast {0}".format(testcase))
        for file in filetowrite:
            os.system("rm {0}".format(file))
    if wrong == True:
        break
