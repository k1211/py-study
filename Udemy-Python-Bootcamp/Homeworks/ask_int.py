def ask_int():
    while True:
        try:
            num = int(raw_input("Enter an integer: "))
        except:
            print "That was not an integer"
            continue
        else:
            print num ** 0.5
            break
        finally:
            print "All done"

ask_int()
