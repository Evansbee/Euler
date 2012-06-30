
base = [0,1,2,3,4,5,6,7,8,9]

for a in range(10):
    p1 = list(base)
    entry = ""
    entry += str(p1[a])
    for b in range(9):
        p2 = list(p1)
        p2.remove(p1[a])
        entry += str(p2[b])

        for c in range (8):
            p3 = list(p2)
            p3.remove(p2[b])
            entry += str(p3[c])

            for d in range (7):
                p4 = list(p3)
                p4.remove(p3[c])
                entry += str(p4[d])

                for e in range (6):
                    p5 = list(p4)
                    p5.remove(p4[d])               
                    entry += str(p5[e])

                    for f in range (5):
                        p6 = list(p5)
                        p6.remove(p5[e])
                        entry += str(p6[f])

                        for g in range (4):
                            p7 = list(p6)
                            p7.remove(p6[f])
                            entry += str(p7[g])

                            for h in range (3):
                                p8 = list(p7)
                                p8.remove(p7[g])
                                entry += str(p8[h])

                                for i in range (2):
                                    p9 = list(p8)
                                    p9.remove(p8[h])
                                    entry += str(p9[i])

                                    for j in range (1):
                                        p10 = list(p9)
                                        p10.remove(p9[i])
                                        entry += str(p10[j])
                                        print entry
