# HW : File handling menu driven our batch xsv file add delete read edit student

def addDetails():
    f = open("C:\\ROYAL\\ALAKH SIR PYTHON\\IMS\\Concepts\\ourBatch.csv", "r")

    data = f.readlines()

    f.close()

    f = open("C:\\ROYAL\\ALAKH SIR PYTHON\\IMS\\Concepts\\ourBatch.csv", "w")

    rno = input("Enter Roll No : ")
    name = input("Enter Name : ")
    role = input("Enter Role : ")

    data.append(f"\n{rno},{name},{role}")

    f.writelines(data)

    print("\nData Added Successfully")

    f.close()


def displayDetails():
    disp_flag = False
    f = open("C:\\ROYAL\\ALAKH SIR PYTHON\\IMS\\Concepts\\ourBatch.csv", "r")

    data = f.readlines()

    rno = input("Enter Roll No : ")

    for row in data:
        temprow = row.rstrip()
        rowData = temprow.split(',')
        if rno == rowData[0]:
            print(f"\nRoll No : {rowData[0]}")
            print(f"Name    : {rowData[1]}")
            print(f"Role    : {rowData[2]}")
            disp_flag = True
        else:
            pass

    if not disp_flag:
        print(f"Does Not Have Any Data With Roll No {rno}")

    f.close()


def editDetails():
    edit_flag = False
    f = open("C:\\ROYAL\\ALAKH SIR PYTHON\\IMS\\Concepts\\ourBatch.csv", "r")

    data = f.readlines()

    rno = input("\nEnter Roll No : ")

    for row in data:
        temprow = row.rstrip()
        rowData = temprow.split(',')
        if rno == rowData[0]:
            print(f"{temprow}")
            print("\nWhat You Want To Change ")
            print("1---Roll No")
            print("2---Name")
            print("3---Role")
            choice = int(input("Enter your Choice : "))
            match choice:
                case 1: rowData[0] = input("\nEnter New Roll No : ")
                case 2: rowData[1] = input("\nEnter New Name : ")
                case 3: rowData[2] = input("\nEnter New Role : ")
                case _: print("Invalid Choice!!")
            newrow = rowData[0] + "," + rowData[1] + "," + rowData[2] + "\n"
            index = data.index(row)
            data[index] = newrow
            edit_flag = True

        else:
            pass

    if not edit_flag:
        print(f"Does Not Have Any Data With Roll No {rno}")

    f.close()
    if edit_flag:
        f = open("C:\\ROYAL\\ALAKH SIR PYTHON\\IMS\\Concepts\\ourBatch.csv", "w")

        f.writelines(data)

        print("\nData Updated Successfully")

        f.close()


def deleteDetails():
    del_flag = False
    f = open("C:\\ROYAL\\ALAKH SIR PYTHON\\IMS\\Concepts\\ourBatch.csv", "r")

    data = f.readlines()

    rno = input("\nEnter Roll No Whose Detail You Want To Delete: ")

    for row in data:
        temprow = row.rstrip()
        rowData = temprow.split(',')
        if rno == rowData[0]:
            data.remove(row)
            del_flag = True
        else:
            pass
    if not del_flag:
        print(f"\nDoes Not Have Any Data With Roll No {rno}")

    f.close()
    if del_flag:
        f = open("C:\\ROYAL\\ALAKH SIR PYTHON\\IMS\\Concepts\\ourBatch.csv", "w")

        f.writelines(data)

        print("\nData Deleted Successfully")

        f.close()


while True:
    print("\n1---Add Details")
    print("2---Display Details")
    print("3---Edit Details")
    print("4---Delete Details")
    print("5---Exit")
    choice = int(input("Enter Your Choice : "))

    match choice:

        case 1: addDetails()
        case 2: displayDetails()
        case 3: editDetails()
        case 4: deleteDetails()
        case 5: break
        case _: print("Invalid Choice!!")
