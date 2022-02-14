def main():
    example1 = "Computer Science 151, Computer Science 415, Computer Science 490"
    example2 = example1.replace("Computer Science","comp")

    course_list = ["Computer Science 151","Computer Science 152","Computer Science 206","Computer Science 415","Computer Science 490","Computer Science 460"]
    middle_courses = course_list[2:4]

    for course in course_list:
        course = course.replace("Computer Science","comp")
        print(f"let's teach {course}")

    #print(example1.upper())
    #print(example1)
    #print(example2)
    #print(middle_courses)



main()