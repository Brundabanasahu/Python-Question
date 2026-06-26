day=input()
n=int(input())
mp = {
    "sun": 7,
    "mon": 6,
    "tue": 5,
    "wed": 4,
    "thu": 3,
    "fri": 2,
    "sat": 1
}
firstsunday=mp[day]

if n<firstsunday:
    print(0)
else:
    print(1+(n-firstsunday)//7)    