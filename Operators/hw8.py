score1 = float(input("1-ci imtahan balinizi daxil edin: "))
score2 = float(input("2-ci imtahan balinizi daxil edin: "))
score3 = float(input("3-cu imtahan balinizi daxil edin: "))


average_score = (score1 + score2 + score3) / 3
print("Orta bal:", average_score)


if average_score > 90:
    print("ela!")

elif 70 < average_score <= 90:
    print("Yaxsi")

elif 50 < average_score <= 70:
    print("Kafi")

else:
    print("Zeif")
