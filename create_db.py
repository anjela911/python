import sqlite3
conn = sqlite3.connect("quiz_user_detail.db")
c = conn.cursor()
c.execute("""drop table quiz""")
c.execute("""drop table question""")
c.execute("""CREATE TABLE IF NOT EXISTS QUIZ(QUIZ_ID INT PRIMARY KEY,QUIZ_NAME TEXT,TOTAL_QUES INT)""")
c.execute("INSERT INTO  QUIZ(QUIZ_ID,QUIZ_NAME,TOTAL_QUES)VALUES(1,'PYTHON',3)")
c.execute("INSERT INTO  QUIZ(QUIZ_ID,QUIZ_NAME,TOTAL_QUES)VALUES(2,'GK',3)")
c.execute("INSERT INTO  QUIZ(QUIZ_ID,QUIZ_NAME,TOTAL_QUES)VALUES(3,'DATABASE',3)")
conn.execute("COMMIT")
c.execute("""CREATE TABLE IF NOT EXISTS QUESTION(QUES_ID INT PRIMARY KEY,QUES_NAME TEXT,OPTION TEXT,CORR_ANS TEXT, 
Q_ID INT,FOREIGN KEY(Q_ID) REFERENCES QUIZ(QUIZ_ID))""")

c.execute("""INSERT INTO  QUESTION(QUES_ID,QUES_NAME,OPTION,CORR_ANS,Q_ID)VALUES(11, "Which method is used to Commit pending transaction to the database in Python?","1.connection.commit(),2.cursor.commit()","1.connection.commit()",1)""")
c.execute("""INSERT INTO  QUESTION(QUES_ID,QUES_NAME,OPTION,CORR_ANS,Q_ID)VALUES(12,"In Python 3, the maximum value for an integer is 263 - 1?","1.FALSE,2.TRUE","1.FALSE",1)""")
c.execute("""INSERT INTO  QUESTION(QUES_ID,QUES_NAME,OPTION,CORR_ANS,Q_ID)VALUES(13,"What is the correct file extension for Python files ?","1.'.pyt',2..py,3..pt","2..py",1)""")
c.execute("""INSERT INTO  QUESTION(QUES_ID,QUES_NAME,OPTION,CORR_ANS,Q_ID)VALUES(21,"Who among the following is known for his work on medicine during the Gupta period?","1.Saumilla,2.Shaunaka,3.Susrutha","3.Susrutha",2)""")
c.execute("""INSERT INTO  QUESTION(QUES_ID,QUES_NAME,OPTION,CORR_ANS,Q_ID)VALUES(22,"Which of the following rivers is most mentioned in early Vedic literature?","1.Ganga,2.Sindhu,3.Sarasvati","2.Sindhu",2)""")
c.execute("""INSERT INTO  QUESTION(QUES_ID,QUES_NAME,OPTION,CORR_ANS,Q_ID)VALUES(23,"Who among the followings decipher Ashokan inscriptions?","1.Buhler,2.Robert Sewell,3.James Prinsep","3.James Prinsep",2)""")
conn.execute("COMMIT")
c.execute("""SELECT * FROM QUIZ""")
obj_quiz = c.fetchall()
row_cnt =len(obj_quiz)
rc = 0
while rc < row_cnt:
    quiz_nm = obj_quiz[rc][0]
    # print(quiz_nm)
    rc = rc + 1
# option_quiz = int(input('choose your quiz subject :1,2 or 3'))
# if int(quiz_nm) == option_quiz:
# an = option_quiz
# c.execute("""SELECT * FROM QUIZ WHERE QUIZ_ID =?""", an)
# q_option = c.fetchone()
# print (q_option)
# else:
# print("incorrect option")
# c.execute("""SELECT * FROM QUESTION WHERE Q_ID =?""",q_option)
c.execute("""SELECT * FROM QUESTION WHERE Q_ID =(SELECT QUIZ_ID FROM QUIZ WHERE QUIZ_NAME =?)""",('PYTHON',))
obj = c.fetchall()

row_count = len(obj)
i = 0
while i < row_count:
    ques = obj[i][1]
    option = obj[i][2]
    corr_ans = obj[i][3]
    #print(ques)
    #print(option)
    #print (corr_ans)
    #print(corr_ans[0])
    i=i+1
    score = 0
    for l in range(3):
        print(ques)
        for op in option:
            print(option)
        answer = int(input('\nenter ur choice'))
        if int(corr_ans[0]) == answer:
            print("\nYou are correct")
            score += 1
        else:
            print("\nYou are incorrect")
        print(f'\nFINAL SCORE: {score}')








