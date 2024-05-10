from datetime import datetime
import os
import subprocess
import sys
import time

# Variables
desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')


# 'https://stackoverflow.com/questions/4417546/constantly-print-subprocess-output-while-process-is-running'
# function to execute a supplied command as a subprocess of this script
def zimmermanExecute(command):
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    print(f"[+] Parsing with your supplied options: {command}.")
    
    while True:
        nextline = process.stdout.readline()
        result = process.poll()
        if result is not None: 
            process.terminate()
            break
        else:
            sys.stdout.write(nextline.decode('utf8'))
  
    print(f"[+] DONE parsing with your supplied options: {command}.\n")
    print("Please check the Desktop for the parsed CSV output file.\n")
        
    #Poll process for new output until finished
    # while True:
        # nextline = process.stdout.readline()
        # if nextline == '' and process.poll() is not None:
            # break
        # sys.stdout.write(nextline.decode('utf8'))


    # output = process.communicate()[0]
    # exitCode = process.returncode

    # if (exitCode == 0):
        # return output
    # else:
        # raise ProcessException(command, exitCode, output)


while True:
    # Initial Menu for user to pick from.
    while True:
        inputArtifactChoiceList = ["1", "2", "3", "4", "5", "6", "7"]
        print("\nAll parsed artifacts will be output to the Desktop as a CSV file.\n")
        artifact = input("""Enter a number from the menu below.\n1. Windows Event Logs\n2. MFT\n3. MFT Timeline\n4. SRUM\n5. Prefetch\n6. Amcache\n7. IIS Logs\n\nChoice: """)

        if artifact in inputArtifactChoiceList:
            break
        else:
            print("Please enter a valid option.\n")


    # WINDOWS EVENT LOGS LOGIC
    if artifact == "1":
        # Initilize an argument string to be fed into ZimmermanTool
        arguments = " "

        # Define path of EvtxECmd.exe
        cwd = os.path.join(os.getcwd(), 'ZimmermanTools\\', 'EvtxECmd\\')
        zimmermanExePath = os.path.join(cwd, 'EvtxECmd.exe')
        
        # Get hostname of asset being analyzed
        hostname = input("Enter hostname you are analyzing: ")

        
        # Define output csv filename
        csvf = "evtx_" + hostname + ".csv"
       
        # Determine if it is a directory or file that needs to be parsed.
        inputTypeChoiceList = ["d", "directory", "f", "file"]
        while True:
            inputTypeChoice = input("""Parsing a directory or a file?\nEnter "d" for directory or "f" for file: """)

            if inputTypeChoice.lower() in inputTypeChoiceList:
                break

            else:
                print("Please enter a valid option.\n")

        # Intialize input arguments for ZimmermanTools
        if inputTypeChoice.lower() == "d":
            dir = input("Enter directory path: ")
            arguments = arguments + "-d" + " " + '"' + dir + '"'
        if inputTypeChoice.lower() == "f":
            f = input("Enter file path: ")
            arguments = arguments + "-f" + " " + '"' + f + '"'

        # Determine if a specific timerange is desired.
        inputTimeChoiceList = ["t", "a"]
        while True:
            inputTime = input('Need a specific a timerange? Or do you want the entire input parsed?\nEnter "t" for a specific timerange or "a" for all timeranges: ')

            if inputTime.lower() in inputTimeChoiceList:
                break

            else:
                print("Please enter a valid option.\n")

        # If timerange is selected, have user define start and end times.
        if inputTime == "t":
            while True:
                inputStartTime = input('Start time (yyyy-MM-dd): ')
                inputEndTime = input('End time (yyyy-MM-dd): ')

                # Input validation
                timeFormat = "%Y-%m-%d"

                try:
                    if bool(datetime.strptime(inputStartTime, timeFormat)) and bool(datetime.strptime(inputEndTime, timeFormat)):
                        # Intialize sd and ed input arguments for ZimmermanTools
                        sd = inputStartTime
                        ed = inputEndTime
                        arguments = arguments + " " + "--sd" + " " + sd + " " + "--ed" + " " + ed
                        break
                except ValueError:
                    print("Please enter a valid option.\n")
                else:
                    print("Please enter a valid option.\n")
                    
        # Construct final command
        arguments = arguments + " " + "--csv" + " " + desktop + " " + "--csvf" + " " + csvf
        command = zimmermanExePath + arguments

        # Execute Zimmerman Tool
        zimmermanExecute(command)


    # MFT LOGIC

    # MFT TIMELINE LOGIC

    # SRUM LOGIC

    # PREFETCH LOGIC

    # AMCACHE LOGIC

    # IIS Logs
