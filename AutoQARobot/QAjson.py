import json
with open(r"C:\Users\77329\source\repos\AutoQARobot\AutoQARobot\Answers.txt") as f:
    answers = ''.join(f.readlines()).split('***')
    answers_len = len(answers)
    answers_dict = {}
    for i in range(answers_len):
        answers_dict[i] = answers[i]
    with open(r"C:\Users\77329\source\repos\AutoQARobot\AutoQARobot\Answers.json", "w") as f_1:
        json.dump(answers_dict, f_1)
        f_1.close()
    f.close()
    

