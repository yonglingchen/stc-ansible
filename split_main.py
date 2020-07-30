
import os

for i in range(0,9):
    if os.path.exists("new_main_" + str(i) + ".yaml"):
        os.remove("new_main_" + str(i) + ".yaml")

with open("main.yaml") as lines:
    i = 1
    file_name = "new_main_0.yaml"
    for line in lines:
        if "name" in line:
            file_name = "new_main_" + str(int(i/10)) + ".yaml"
            with open(file_name, 'a') as o:
                if i%10 == 0:
                    print(i)
                    o.write("-\n")
                    o.write("\n")
                    o.write("  hosts: rtp-ls\n")
                    o.write("\n")
                    o.write("  tasks:\n")
                    o.write("\n")
            i += 1
        with open(file_name, 'a') as o:
            o.write(line)

