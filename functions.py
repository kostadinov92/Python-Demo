def print_temperature(temp):
    print(temp, 'C')

def print_temperature(temp):
    print(temp, 'Це')

print_temperature(4643) # Це


def convert_fahrenheit_to_celsius(deg_f):
    return (deg_f - 32) / 1.8


def print_temperature(temp):
    print(temp, 'Це')

print(convert_fahrenheit_to_celsius(45))

result = print_temperature(355)
print('>>> ', result)

# -------------------


def div_mod(number, divisor):   # по някаква причина вградената функция divmod не ни харесва :о)
    result = number // divisor
    modulus = number % divisor
    return (result, modulus)  # връщаме tuple ;    може да се запише и без скобите - return result, modulus

neshto = div_mod(13, 3)
print('Neshto: ', neshto)  # отпечатва върнатия tuple   -  (4, 1)

# по-удобно
r, m = div_mod(13, 3)
print(r)   # отпечатва 4
print(m)  # отпечатва 1

# -------------------------------------

variable = 1,

print(variable)
print(len(variable))

# ------------------------------------------

def print_greeting(name="everybody"):
    print("Hello, ", name)

print_greeting("Boris")
print_greeting()

# ----------------------------------------------

def send_email(subject,
               to_email,
               body=None,
               from_email='boris@sentido.bg',
               cc_email=None,
               attachments=None):
    print("Sending email from {} to {}".format(
        from_email,
        to_email
    )
)

send_email(
    from_email="gatakka@example.com",
    to_email="boris.chervenkov@example.com",
    subject="Лекция за функции - за курса по Python",
    cc_email="gatakka@example.com",
    body="Здрасти, готови ли сме с лекцията за функции, или още не сме я написали?",
)

send_email(
    subject="Лекция за функции - за курса по Python",
    to_email="boris.chervenkov@example.com",
)

# ----------------------------------------------

def sum_numbers(*args):   # args ще бъде tuple, който ще съдържа стойностите на всички подадени позиционни параметри
    total = 0
    for n in args:
        total += n
    return total


print(sum_numbers(1))
print(sum_numbers(1, 3, 4, 5, 6, 7, 88))

# -------------------------------------------------

def pretty_print_record(**kwargs):   # във функцията kwargs ще бъде обикновен dict
    print("Record:")
    for k, v in kwargs.items():
        print("\t", k, "= ", v)

pretty_print_record(name="Mercury", distance_au=0.387, diameter_km=4878)
pretty_print_record(name="Venus", distance_au=0.723, diameter_km=12104)
pretty_print_record(name="Earth", distance_au=1, diameter_km=12742, average_temp_c=7.2, atmosphere=["nitrogen", "oxygen", "argon"])
pretty_print_record()


# ----------------------------------------------

'{} {} {name}'.format(432, 44, name='Boris')


def format_with_indent(format_string, *args, indent: int=None, indent_with: str=" ", **kwargs):
    if indent is not None:
        indent_str = indent_with * indent  # will multiply the indent string
    else:
        indent_str = ""

    return indent_str + format_string.format(*args, **kwargs)

...

print(format_with_indent("Name: {}, Role: {role}", 'Boris', role='lecturer'))

print(format_with_indent("Name: {}, Role: {role}", 'Boris', role='lecturer', indent=4))

print(format_with_indent("Name: {}, Role: {role}", 'Boris', role='lecturer', indent=4, indent_with='-'))

# -----------------------------------------------------------

def convert_fahrenheit_to_celsius(deg_f: float) -> float:
    return (deg_f - 32) / 1.8

print(convert_fahrenheit_to_celsius(234.45))


def convert_fahrenheit_to_celsius(deg_f: float) -> float:
    return (deg_f - 32) / 1.8


def convert_fahrenheit_to_celsius(deg_f: float) -> float:
    return (deg_f - 32) / 1.8

x = 5
x = 6


convert_elephants_to_penguins = convert_fahrenheit_to_celsius

print(convert_fahrenheit_to_celsius(54))
print(convert_elephants_to_penguins(54))

# ------------------------------------------------------

def convert_fahrenheit_to_celsius(degrees_f):
    degrees_c = (degrees_f - 32) / 1.8
    return degrees_c

print(convert_fahrenheit_to_celsius(32))
print(degrees_c)  # грешка - променливата degrees_c е дефинирана във функцията, и тук не съществува
print(degrees_f)  # грешка - degrees_f е параметър на функцията, и тук не съществува


# -----------------------------------------------


MAX_VALUE = 5


def calculate(number):
    if number > MAX_VALUE:
        return None
    else:
        return number ** 2

print(calculate(4))


# ---------------------------------

number_of_calculations_performed = 0  # глобална променлива

def calculate(parameter1, parameter2):
    ...
    global number_of_calculations_performed

    # print(number_of_calculations_performed)
    number_of_calculations_performed = number_of_calculations_performed + 1   # грешка

calculate(4, 5)
print(number_of_calculations_performed)


# ------------------


number_of_calculations_performed = 10  # глобална променлива

def calculate(parameter1, parameter2):
    ...

    # print(number_of_calculations_performed)
    number_of_calculations_performed = 23
    print("In the function: ", number_of_calculations_performed, id(number_of_calculations_performed))


print('Before: ', number_of_calculations_performed)
calculate(4, 5)
print('After: ', number_of_calculations_performed)

# ----------------------------

calculations_performed = []  # глобална променлива


def calculate(parameter1, parameter2):
    ...
    # global calculations_performed
    # print(number_of_calculations_performed)
    calculations_performed.append(parameter1 * parameter2)
    print("In the function: ", calculations_performed)

print('Before: ', calculations_performed)
calculate(4, 5)
calculate(40, 2)
calculate(50, 3)
calculate(60, 4)
print('After: ', calculations_performed)