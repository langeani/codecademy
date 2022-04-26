last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]
#codecademy's project grade_book
subjects = ["physics", "calculus", "poetry", "history"]
grades = [98,97,85,88]
gradebook = [["physics", 98], ["calculus", 97], ["poetry", 85], ["history", 88]]

gradebook.append(["computer_science"])
gradebook[-1].append(100)

gradebook.append(["visual arts"])
gradebook[-1].append(93)

#modify visual arts points do 98
gradebook[-1][-1] = 98

#find the grade in poetry class, .remove() and .ppend() to "Pass"
gradebook[2].remove(85)
gradebook[2].append("Pass")

print("This are your grades from this semester: " + str(gradebook))

full_gradebook = last_semester_gradebook + gradebook
print("Both semester's grades: " + str(full_gradebook))
