print("Welcome to the Caesar Cipher!")

choice = input("Do you want to Encrypt or decrypt? (e/d): ")

if choice != 'e' and choice != 'd':
    print("Invalid option. exiting program.")
else:
   
    message = input("Enter your Message: ")
    shift_input = input("Enter shift number: ")

    if shift_input.strip().isdigit():
        shift = int(shift_input)
    else:
      
        print("Shift was not a valid number. Using 0 as default.")
        shift = 0

    result = ""

    for char in message:
       
        if char.isalpha():
            
            if char.isupper():
                base = ord('A')
            else:
                base = ord('a')

          
            if choice == 'e':
                new_char = chr((ord(char) - base + shift) % 26 + base)
            else:
                new_char = chr((ord(char) - base - shift) % 26 + base)

            result = result + new_char

        else:
            result = result + char

    print("Result is:", result)
