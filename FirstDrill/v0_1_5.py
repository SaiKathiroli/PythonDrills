import time

LOGS = [
    "2024-01-15 08:23:41 ERROR    database Connection timeout after 30s",
    "2024-01-15 08:24:01 WARNING  auth     Failed login attempt for user admin",
    "2024-01-15 08:24:15 INFO     server   Request received from 192.168.1.1",
    "2024-01-15 08:25:03 ERROR    database Connection timeout after 30s",
    "2024-01-15 08:25:11 INFO     auth     User admin logged in successfully",
    "2024-01-15 08:25:45 ERROR    server   Disk usage at 95%",
    "2024-01-15 08:26:02 WARNING  database Slow query detected: 4.2s",
    "2024-01-15 08:26:18 INFO     server   Health check passed",
    "2024-01-15 08:27:00 ERROR    auth     Account locked: too many failures",
    "2024-01-15 08:27:33 WARNING  server   Memory usage at 80%",
]

q = ["by_level","sources","error_count","most_recent"]
w = dict.fromkeys(q)
w["by_level"]= dict()
print(w)
source = list()
most_recent = {}
final_lists = []

start = time.perf_counter()

for _ in LOGS:
    x = _.split(" ",maxsplit=3)
    x = [t.strip() for t in x]
    y = x[-1]
    x.pop()
    x.extend(y.split(" ",maxsplit=1))
    x = [t.strip() for t in x]
    print(x)
    final_lists.append(x)
    #####################################
    if x[2] not in w["by_level"]:
        w["by_level"][x[2]] = [x[4]]
        pass
    else:
        w["by_level"][x[2]].append(x[4])
        pass
    ####################################
    source.append(x[3])


print(w)
source = set(source)
print(source)
end = time.perf_counter()
print(f"Errors: {len(w["by_level"]["ERROR"])}")


for details in final_lists[::-1]:
    if details[2] not in most_recent:
        most_recent[details[2]] = {"timestamp":details[0] + " " + details[1], "Source":details[3], "Message":details[4]}
    else:
        continue

print(most_recent)

print(end-start)
