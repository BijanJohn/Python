#Bijan Rahnamai SYN: 26102
#Lab 8
#Desc
#7/20/2017

def main():
    #Local variables
    digit_list = ['2','3','4','5','6','7','8','9']

    #set up string variables
    alpha_phone_number = ''
    num_phone_number = ''
    #Get the string as input from the user.
    alpha_phone_number = input('Enter the telephone' \
                               'number in the format' \
                               ' (XXX)-XXX-XXXX: ')
    #Error checking, alphanumeric , ( , ) , -
    no_special_character = True
    no_white_space = True
    for ch in alpha_phone_number:
        if ch == '!' or ch == '@' or ch == '#' or ch == '$' or ch == '%' or ch == '^' or ch == '&' or ch == '*' or ch == '_' or ch == '+' or ch == '=' or ch == ':' or ch == ';' or ch == '<' or ch == '>' or ch == '.' or ch == '/' or ch == '?' or ch == ',' or ch == '[' or ch == ']' or ch == '{' or ch == '}' or ch == '|':
            no_special_character = False
        if ch == ' ':
            no_white_space = False
        while no_white_space == False or no_special_character == False:
            print('Please correct your format')
            alpha_phone_number = input('Enter the telephone' \
                                   'number in the format' \
                                   ' (XXX)-XXX-XXXX: ')
    #alpha_phone_number = alpha_phone_number.rstrip(')')
    #alpha_phone_number = alpha_phone_number.lstrip('(')
    alpha_phone_number = alpha_phone_number.strip('-')
    print(alpha_phone_number)
    if 10 > len(alpha_phone_number) or 10 < len(alpha_phone_number):
        print('Please check your format')

    if no_white_space == True and no_special_character == True:
        print('Thanks')
    #convert characters to uppercase
    alpha_phone_number = alpha_phone_number.upper()
    character_tracking = 0
    #Step through the string finding the index number
    #from the digit list for each character. Build the
    #string, and display the digits.
            #Strip them out
        #Check length = 10
    #num_phone_number = []
    #Set the character to a digit from the list.
    for char in alpha_phone_number:
        if char == 'A' or char == 'B' or char == 'C':
            num_phone_number = num_phone_number + "2"
        elif char == 'D' or char == 'E' or char == 'F':
            num_phone_number = num_phone_number + "3"
        elif char == 'G' or char == 'H' or char == 'I':
            num_phone_number = num_phone_number + "4"
        elif char == 'J' or char == 'K' or char == 'L':
            num_phone_number = num_phone_number + "5"
        elif char == 'M' or char == 'N' or char == 'O':
            num_phone_number = num_phone_number + "6"
        elif char == 'P' or char == 'Q' or char == 'R' or char == 'S':
            num_phone_number = num_phone_number + "7"
        elif char == 'T' or char == 'U' or char == 'V':
            num_phone_number = num_phone_number + "8"
        elif char == 'W' or char == 'X' or char == 'Y' or char == 'Z':
            num_phone_number = num_phone_number + "9"
            #Determine the index number for the character
            #Set the character to a digit from the list.
        #Concatenate the digit to the string.
        num_phone_number =  num_phone_number + char
    a_number = num_phone_number.replace('A','')
    b_number = a_number.replace('B','')
    c_number = b_number.replace('C','')
    d_number = c_number.replace('D','')
    e_number = d_number.replace('E','')
    f_number = e_number.replace('F','')
    g_number = f_number.replace('G','')
    h_number = g_number.replace('H','')
    i_number = h_number.replace('I','')
    j_number = i_number.replace('J','')
    k_number = j_number.replace('K','')
    l_number = k_number.replace('L','')
    m_number = l_number.replace('M','')
    n_number = m_number.replace('N','')
    o_number = n_number.replace('O','')
    p_number = o_number.replace('P','')
    q_number = p_number.replace('Q','')
    r_number = q_number.replace('R','')
    s_number = r_number.replace('S','')
    t_number = s_number.replace('T','')
    u_number = t_number.replace('U','')
    v_number = u_number.replace('V','')
    w_number = v_number.replace('W','')
    x_number = w_number.replace('X','')
    y_number = x_number.replace('Y','')
    z_number = y_number.replace('Z','')
    #Display the phone number's digits.
    print('The phone number is', z_number)

#Call the main function.
main()
