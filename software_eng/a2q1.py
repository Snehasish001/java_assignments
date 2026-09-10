
def type_of_project(KLOC: float) -> str:
    if KLOC < 50:
        return 'Organic'
    elif KLOC < 300:
        return 'Semi-detached'
    else:
        return 'Embedded'

def effort_to_develop(KLOC: float, a: float, b: float) -> float:
    return a * KLOC ** b

def time_to_develop(KLOC: float, a: float, b: float, c: float, d: float) -> float:
    return c * effort_to_develop(KLOC, a, b) ** d

def number_of_people(KLOC: float, a: float, b: float, c: float, d: float):
    return effort_to_develop(KLOC, a, b) // time_to_develop(KLOC, a, b, c, d)

def main() -> None:
    constant_factors = {
        'Organic' : [2.4, 1.05, 2.5, 0.38],
        'Semi-detached' : [3.0, 1.12, 2.5, 0.35],
        'Embedded' : [3.6, 1.20, 2.5, 0.32]
    }

    KLOC = int(input('Enter lines of code : '))

    type_project = type_of_project(KLOC)

    print(F"Type of project   : {type_project}")
    print(F"Effort to develop : {effort_to_develop(KLOC, constant_factors[type_project][0], constant_factors[type_project][1])} Person-Month")
    print(F"Time to develop   : {time_to_develop(KLOC, constant_factors[type_project][0], constant_factors[type_project][1], constant_factors[type_project][2], constant_factors[type_project][3])} Months")
    print(F"Number of people  : {number_of_people(KLOC, constant_factors[type_project][0], constant_factors[type_project][1], constant_factors[type_project][2], constant_factors[type_project][3])} Persons")


if __name__ == "__main__":
    main()