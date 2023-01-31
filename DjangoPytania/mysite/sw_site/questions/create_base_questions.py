import json



with open('questions_json.txt', 'r', encoding='utf-8') as f:
    readed_file = json.load(f)

for question in readed_file:
    print(question)


#  WORKING IN SHELL

# >>> for question in readed_file:
# ...     n1 = question['number_of_question']
# ...     n2 = question['question_content']
# ...     n3 = question['answer_a']
# ...     n4 = question['answer_b']
# ...     n5 = question['answer_c']
# ...     n6 = question['correct_answer']
# ...     n7 = question['notes']
# ...     question_list = [n1, n2, n3, n4, n5, n6, n7]
# ...     ins_q = Question()
# ...     ins_q.create_question(question_list)
# ...     ins_q.save()

# created base of questions