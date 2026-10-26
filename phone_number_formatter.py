def clean_number(text) :
    text = text.replace("-", "")
    text = text.replace(" ", "")
    text = text.replace(".", "")
    return text

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
    print("Type in 'q' to quit.")
    while True :
        phonenum = input("Phone number: ")
        if phonenum == "q" :
            break
        phonenum = clean_number(phonenum)
        if is_valid(phonenum) == None: 
            print("Invalid phone number.")
        else :
            dSum = digit_sum(phonenum)
            phonenum = phonenum[:3] + "-" + phonenum[3:6] + "-" + phonenum[6:]
            print("Formatted: ", phonenum)
            print("Hidden: ", phonenum[:4] + "XXX" + phonenum[7:])
            print("Digit sum: ", dSum)


main()
