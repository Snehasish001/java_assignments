import random


def object_points(screens: int, reports: int, components: int) -> int:

    screen_weight = 3
    report_weight = 8
    component_weight = 10

    return (
        screens * screen_weight +
        reports * report_weight +
        components * component_weight
    )


def new_object_points(op: float, reuse: float) -> float:
    return op * (1 - reuse / 100)


def effort_to_develop(nop: float, productivity: float) -> float:
    return nop / productivity


def total_project_cost(effort: float, labour_rate: float) -> float:
    return effort * labour_rate


def main() -> None:

    # Simulated input
    screens = random.randint(10, 20)
    reports = random.randint(5, 10)
    components = random.randint(5, 15)

    reuse = random.randint(70, 95)
    productivity = random.randint(20, 30)
    labour_rate = random.choice([1200, 1500, 1800, 2000])

    print("\n--- Simulated Input ---")
    print(f"Number of Screens   : {screens}")
    print(f"Number of Reports   : {reports}")
    print(f"Number of Components: {components}")
    print(f"Reuse               : {reuse}%")
    print(f"Productivity        : {productivity} OP/Person-Month")
    print(f"Labour Rate         : ₹{labour_rate}/Person-Month")

    # Object Points
    op = object_points(
        screens,
        reports,
        components
    )

    # New Object Points
    nop = new_object_points(
        op,
        reuse
    )

    # Effort
    effort = effort_to_develop(
        nop,
        productivity
    )

    # Cost
    cost = total_project_cost(
        effort,
        labour_rate
    )

    print("\n--- Application Composition Result ---")
    print(f"Object Points      : {op:.2f}")
    print(f"New Object Points  : {nop:.2f}")
    print(f"Effort             : {effort:.2f} Person-Month")
    print(f"Total Project Cost : ₹{cost:.2f}")


if __name__ == "__main__":
    main()