open file
open temp_file
for read lines:
    if line contains plotly:
        add whitespace for 'seamless' tag
        add link="False" autosize="True"
    write line to temp_file
move file to backup
move temp_file to file
