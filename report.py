def print_report_rus(total, user, action, sessions, top, unique_action_user, action_per_user):

    print("Общее количество событий ->", total)
    print()

    print("Количество событий по пользователям ->", user)
    print()

    print("Количество событий по типу действия ->", action)
    print()

    print("Количество уникальных действий у пользователя ->", unique_action_user)
    print()

    print("Пользователь → действия → количество -|", action_per_user)
    print()

    print("Топ пользователей по активности:")

    # for i, (user, count) in enumerate(top, 1):
    #     print(i, user, count)

    print()
    print("Сессии:")

    for user, count in user.items():

        s = sessions.get(user, {"completed": 0, "incomplete": 0})

        completed = s["completed"]
        incomplete = s["incomplete"]

        print(user, f"{completed} completed, {incomplete} incomplete")

    print()



def print_report(total, user, action, sessions, top):

    print("======= REPORT =========")

    print("Total events:", total)

    print()
    print("Users activity:")

    for user, count in user.items():

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

    for action, count in action.items():
        print(f"- {action}: {count}")

    print()
    print("Top users:")

    for i, (user, count) in enumerate(top, 1):
        print(f"{i}. {user} — {count} events")


 



        