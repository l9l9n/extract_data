def print_report(total, by_user, by_action, sessions, top):

    print("===== REPORT =====\n")

    print("Total events:", total)
    print()

    print("Users activity:")

    for user, count in by_user.items():

        s = sessions.get(user, {"completed": 0, "incomplete": 0})

        completed = s["completed"]
        incomplete = s["incomplete"]

        print(
            f"- {user}: {count} events "
            f"({completed + incomplete} sessions: "
            f"{completed} completed, {incomplete} incomplete)"
        )

    print()

    print("Actions summary:")

    for action, count in by_action.items():
        print(f"- {action}: {count}")

    print()

    print("Top users:")

    for i, (user, count) in enumerate(top, 1):
        print(f"{i}. {user} — {count} events")

        