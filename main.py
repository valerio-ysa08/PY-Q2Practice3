from pyscript import document, display
# Use document if there is a form

def checkNum (e):

    num_bers = ["9", "8", "7", "6", "5"]

    num1 = document.getElementById("num1").value
    name = "Ysaaa" # extra lang po

    confirm_num = num1 in num_bers

    message = (f'Sorry, {name}, your number is invalid.', f'Congrats! {name}, your number is amazing!')
    # First statement = 0 = False | Second Statement = 1 = True

    document.getElementById("output1").innerHTML = message[confirm_num]


