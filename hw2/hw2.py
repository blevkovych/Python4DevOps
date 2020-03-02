import os, sys, json

#Task: There are a set of JSON-files that contains answers from the CI server. An example of such is attached.
#Create a program that returns JSON-file which contains 'id', 'number', 'committer_name' and 'committer_email'
#rom last of failed builds (in other words - with the highest value of 'number' and non-zero 'result').

#How it works: it reads all files in the folder which ends with .json
# and writes on the file the necessary information like this:
# {"id": 22, "number": "34", "committer_name": "Some Commiter", "committer_email": "some.commiter@gmail.com"}

#Command: python hw2.py Jsonfiles result.json

folder = sys.argv[1]
file = sys.argv[2]

for root, dirs, files in os.walk(folder):
    for names in files:
        if names.endswith('.json'):
            inputfile = open(os.path.join(root, names), "r")
            outputfile = open(file, "a")
            data = json.load(inputfile)

            num = data['matrix'][0]['number']
            for mat in data['matrix']:
                if mat['result'] != 0:
                    if mat['number'] > num:
                        num = mat['number']
                        result = ["id: " + str(mat['id']),"number: " + str(num),"committer_name: "
                                  + str(data['committer_name']),"committer_email: " + str(data['committer_email'])]
            json.dump(result, outputfile, indent=4)
            result.clear()
            inputfile.close()
            outputfile.close()