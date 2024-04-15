import pickle
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

def showAllProblems():
    for key in problems:
        print(f"Problem: {key} Reps Done: {problems[key].repNum}")

def addProblem(id):
    if id in problems:
        p = problems[id]
        p.addRepetition()
        print(f"completed repitition {p.repNum} for problem {id}")
        if p.isDone():
            del problems[id]
            print(f"Problem {id} is done! Good Job!!")
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

    elif command == "show":
        showAllProblems()
    else:
        if not command.isnumeric():
            print("Enter just a problem number")
        else:
            addProblem(command)
