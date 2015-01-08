import StringCalculator

while True:
    string = raw_input("enter your mathematical expression:\n")
    print string + "=" + str(StringCalculator.eval(string))
