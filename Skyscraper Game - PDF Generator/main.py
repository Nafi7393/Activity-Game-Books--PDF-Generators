import make_qus
import make_ans

answer_page_num = int(input("How many answer page you want\n1 means having total of 4 pages: \n"))
number_show = int(input("How many numbers you wan to show on answer: "))

make_qus.make_qus_page(page_num=answer_page_num, show_num=number_show, qus_output_name="QUESTION")
make_ans.solution(ans_output_name="ANSWER")


