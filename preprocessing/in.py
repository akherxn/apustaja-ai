with open('in.txt') as input_file:
    with open('out.csv','a') as output_file:
        txt_line = input_file.readline()
        while txt_line:
            cells = txt_line.split("====================")
            
            # Do something with each cell...
            
            csv_line = ";".join(cells)
            
            output_file.write(csv_line)
            txt_line = input_file.readline()