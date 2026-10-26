def clean_number(text) :
    text = text.replace("-", "")
    text = text.replace(" ", "")
    text = text.replace(".", "")
    return text

    # try :
    #     text = int(text)
    # except ValueError :
    #     return None
    # text = str(text)
    # return text

def is_valid(number) :
    if len(number) != 10 or number[0] != "0" :
        return None
    try :
        number = int(number)
    except ValueError :
        return None
    return number

def digit_sum(num) :
    d_sum = 0
    num = int(num)
    while num > 0 :
        digit = num % 10
        d_sum += digit
        num = num // 10
    return d_sum

def main() :
    while True :
        phonenum = input("Phone number: ")
        if phonenum == "q" :
            break
        phonenum = clean_number(phonenum)
        dSum = digit_sum(phonenum)
        if is_valid(phonenum) == None: 
            print("Invalid phone number.")
        else :
            phonenum = phonenum[:3] + "-" + phonenum[3:6] + "-" + phonenum[6:]
            print("Formatted: ", phonenum)
            hidden = phonenum[:4] + "XXX" + phonenum[7:]
            print("Hidden: ", hidden)
            print("Digit sum: ", dSum)




            
                # print("Formatted: ", phonenum)
                # print("Hidden: ", hidden(phonenum))
                # print("Digit sum: ", digit_sum(phonenum))

main()