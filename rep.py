import pickle
from datetime import datetime
from problem import problem

#Load in list of problems
problems = {}
try:
    problems = pickle.load(open("problems.pickle", "rb"))
except (OSError) as e:
    pickle.dump(problems, open("problems.pickle", "wb"))

def getProblems():
    print("To do: ")
    for p in problems.values():
        if p.isDue():
            print(p.id)

def addProblem(id):
    if id in problems:
        print(f"completed repitition {id.repNum} for problem {id}")
        problems[id].repNum += 1
        problems[id].lastDoneDate = datetime.now()
    else:
        print(f"added problem {id} to the list")
        problems[id] = problem(id)
    pickle.dump(problems, open("problems.pickle", "wb"))

#Listen in the console
while True:
    command = input()

    if command == "exit":
        break
    
    elif command == "get":
        getProblems()
    
    else:
        if not command.isnumeric():
            print("Enter just a problem number")
        else:
            addProblem(command)
