# Opens file. File get's printed. ___ gets treated as input field. input gets written to file at specific location. code gets tested.

QuestionF = open('question.py', 'r')
AnswerF = open('question1.py', 'w')

QStr = QuestionF.read()
QList = QStr.split('___')
print(QList[0], end = "")
answer = input()
print(QList[1])

AStr = QList[0] + answer + QList[1]
AnswerF.write(AStr)

QuestionF.close()
AnswerF.close()
