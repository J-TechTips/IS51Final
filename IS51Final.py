"""
Program will display grades of students on the final by: 
    -number of grades
    -average grade
    -percentage of grades above the average
The average grades is 83.25.
The number of grades is 24.
The percentage of grades above average is 54.17%

We will bring in the list in a dictionary by using the open method.
The grades then will be listed as integers.
Then the calculations can begin.
End result is displaying the 3 solutions.
"""
"""
main()
    starts the program
    infile = open
    display number of grades
    print("")
    display average 
    print("")
    -both done by calculation 

calculate_percent_above_average()
    caluate the percent
    print("")
"""

def main():
    infile = open("Final.txt", 'r')
    finalGrades = [line.rstrip() for line in infile]
    infile.close()
    for i in range(len(finalGrades)):
        finalGrades[i] = int(finalGrades[i])
    len(finalGrades)
    print("Total amount of grades is: ", len(finalGrades))
    gradeAverage = sum(finalGrades) / len(finalGrades)
    print("The average grade is: ", gradeAverage)
    dict = finalGrades
    avg = gradeAverage
    calculate_percent_above_average(dict, avg)

def calculate_percent_above_average(dict, avg):
    num = 0 
    for grade in dict:
        if grade > avg:
            num += 1
    print("The percentage of grades above average: {0:.2f}%".format(100 * num / len(dict)))

main()