import Identify_table
import build_sql
import sql
import logical_ans

val = input("Enter your question: ")

with open('question.txt', 'w') as question_file:
        question_file.write(val)

Identify_table.run()
build_sql.run()
logical_ans.run()
sql.run()