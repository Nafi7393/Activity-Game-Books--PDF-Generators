import make_questions
import output_answers

num_sudoku = int(input("How many Answer sheets you want?\n(1 answer sheets mean 4 sudoku that means total 5 page)\n"))
print(" ")
level = int(input("How many minimum visible number you want?\n(17 is the minimum value you can pass, 81 is highest)\n"))
total_sudoku = num_sudoku * 4


if make_questions.make_sudoku_now(total_sudoku, minimun_visible_number=level, qus_output_name="questions paper"):
    output_answers.solution(total_sudoku, ans_output_name=f"answer paper")
print(f"COMMMMMPLATEEEEEEEE")
