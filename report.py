def print_report_rus(total, user, action, sessions, top, unique_action_user, action_per_user):

    print("Общее количество событий ->", total)
    print()

    print("Количество событий по пользователям ->", user)
    print()

    print("Количество событий по типу действия ->", action)
    print()

    print("Количество уникальных действий у пользователя ->", unique_action_user)
    print()

    print("Пользователь → действия → количество -|")
    for user_n, actions in action_per_user.items():
        print(user_n)

        for action_u, count in actions.items():
            print("   ", action_u, "->", count)

    print()

    print("Топ пользователей по активности:")
    i = 1
    for user_t, count in top:
        print(i, user_t, count)
        i += 1

    print()
    print("Сессии:")

    for username in user.keys():
        stats = sessions.get(username, {"completed": 0, "incomplete": 0})
        
        completed = stats["completed"]
        incomplete = stats["incomplete"]
        
        print(f"{username}: {completed} completed, {incomplete} incomplete")

    print()



def print_report(total, user, action, sessions, top):

    print("======= REPORT =========")

    print("Total events:", total)

    print()
    print("Users activity:")

    for user_s, count in user.items():

        s = sessions.get(user_s, {"completed": 0, "incomplete": 0})

        completed = s["completed"]
        incomplete = s["incomplete"]

        print(
            f"- {user_s}: {count} events "
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


 



        