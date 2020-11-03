from map_coloring import MapColoringProblem, MapColoringConstraint


def test_classes():
    mp = MapColoringProblem(
        {
            "WA": {"red"},
            "NT": {"red", "blue", "green"},
            "SA": {"red", "blue", "green"},
            "Q": {"green"},
            "NSW": {"red", "blue", "green"},
            "V": {"red", "blue", "green"},
            "T": {"red", "blue", "green"}
        }
    )
    for r, cs in {
        "T": {"V"},
        "WA": {"NT", "SA"},
        "NT": {"WA", "Q", "SA"},
        "SA": {"WA", "NT", "Q", "NSW", "V"},
        "Q": {"NT", "SA", "NSW"},
        "NSW": {"Q", "SA", "V"},
        "V": {"SA", "NSW", "T"}
    }.items():
        for pp in cs:
            mp.add_constraint(MapColoringConstraint(r, pp))

    print(mp.backtracking_search())

    variables = ["Western Australia", "Northern Territory", "South Australia", "Queensland", "New South Wales",
                 "Victoria", "Tasmania"]
    domains = {}
    for variable in variables:
        domains[variable] = {"red", "green", "blue"}
    csp = MapColoringProblem(domains)
    csp.add_constraint(MapColoringConstraint("Western Australia", "Northern Territory"))
    csp.add_constraint(MapColoringConstraint("Western Australia", "South Australia"))
    csp.add_constraint(MapColoringConstraint("South Australia", "Northern Territory"))
    csp.add_constraint(MapColoringConstraint("Queensland", "Northern Territory"))
    csp.add_constraint(MapColoringConstraint("Queensland", "South Australia"))
    csp.add_constraint(MapColoringConstraint("Queensland", "New South Wales"))
    csp.add_constraint(MapColoringConstraint("New South Wales", "South Australia"))
    csp.add_constraint(MapColoringConstraint("Victoria", "South Australia"))
    csp.add_constraint(MapColoringConstraint("Victoria", "New South Wales"))
    csp.add_constraint(MapColoringConstraint("Victoria", "Tasmania"))
    print(csp.backtracking_search())
    print(csp.arc_consistency())


if __name__ == "__main__":
    mp = MapColoringProblem(
        {
            "WA": {"red", "green", "blue"},
            "SA": {"red", "green"},
            "NT": {"green"}
        }
    )
    for r, cs in {
        "SA": {"WA", "NT"},
        "NT": {"WA", "SA"}
    }.items():
        for p in cs:
            mp.add_constraint(MapColoringConstraint(r, p))

    print(mp.backtracking_search())
    print(mp.arc_consistency())