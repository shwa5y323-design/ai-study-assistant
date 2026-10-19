print("Welcome to AI Study Assistant!")

while True:
    question = input("Ask a question (or type exit): ").lower()

    if question == "exit":
        print("Good luck with your studies!")
        break
    elif "math" in question:
        print("Math helps us solve problems using logic.")
    elif "physics" in question:
        print("Physics helps us understand energy and motion.")
    elif "ai" in question:
        print("AI helps computers perform intelligent tasks.")
    else:
        print("I am still learning. Try another question!")
