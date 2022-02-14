def main():
    rec_file = open("recommendation.txt",'r')
    lines = rec_file.readlines()
    line_number =0
    for line in lines:
        line_number = line_number +1
        if line_number % 2 == 1:
            print(line)
main()
