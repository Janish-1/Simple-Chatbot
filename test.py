from chatbot import chatbot_question

query = input("Enter a Question: ")
res = chatbot_question("wikipedia"+query)
print(res)