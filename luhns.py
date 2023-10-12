checksum = 0

def checksum_func():
    global checksum
    number = input("Enter a number: ")

    try:
        val = int(number)
        
        num_len = len(number)
        checksum_digit = 0

        def doubled_digit():

            def double():

                global checksum
                doubled_num = (int(number[num]) * 2)

                if (doubled_num >= 10):
                    checksum += int(1 + (doubled_num % 10))
                    print(int(1 + (doubled_num % 10)))

                else:
                    checksum += int(doubled_num)
                    print(int(doubled_num))
            
            for num in range(0, num_len):
                def checksum_add():
                    global checksum
                    checksum += int(number[num])
                    print(int(number[num]))

                if (num_len) % 2 == 0:
                    if (num) % 2 == 0:
                        double()
                    else:
                        checksum_add()
                
                elif (num_len) % 2 == 1:
                    if (num) % 2 == 1:
                        double()
                    else:
                        checksum_add()

        doubled_digit()

        while (checksum) % 10 != 0:
            checksum_digit += 1
            checksum += 1
        
        if (checksum % 10 == 0):
            print("Valid Checksum")
        else:
            print("Invalid Checksum")

        print(checksum_digit)
        print(checksum)

    except (ValueError, TypeError):
        print("Not a number.")
        checksum_func()

checksum_func()


# for num in range(0, num_len):
#     print(rev_num[num])

    #if numberLength % 2 == 0, (num % 2 == 0), else (num % 2 == 1)
    
    #check the length of the number and double even numbers if number has even amount of characters, else double odd
    
    #if numberCheckSum % 10 != 0 tempCheckSum = numberCheckSum: checkDigit++;
    
    #if the total of the numberCheckSum isn't perfectly divisible by 10 add to checkDigit, until it is divisible by 10
    
    #else numberCheckSum = tempCheckSum + checkDigit;
    
    #convert the numberCheckSum to the original number + the checkDigit, achieving divisibility by 10 = 0;

    #if doubled number is > 10 then treat numbers separately as 1 + (doubledNum - 10)
    
    #store number in list, reverse, then multiply the corresponding list number
    
    #How to tell when the number of arbitrary length is complete.
