list = [
    [
        1,2,3,4,5
    ],
    {
        6,7,8,9,10
    },
    [
        "Maca",["apple"]
    ],
    [
        "Banana", ["Banuena"]
    ]
]

print()
print("-+"*20)
print()

print(list[2][1][0])
print(list[3][1][0])
print(list[0][2])

print()
print("-+"*20)
print()


for i in list:
    for l in i:
        print(l)
        if type(l) in list:
            for d in l:
                print(d)