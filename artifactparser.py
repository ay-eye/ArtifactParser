from datetime import datetime
import os
import subprocess

desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop') 
arguments = " "
zimmermanFolder = "./Zimmerman Tools/"

while True:
    # Initial Menu for user to pick from.
    while True:
        inputArtifactChoiceList = ["1", "2", "3", "4", "5", "6", "7"]
        print("All parsed artifacts will be output to the Desktop as a CSV file.")
        artifact = input("Enter a number from the menu below.\n\
                        1. Windows Event Logs\n\
                        2. MFT\n\
                        3. MFT Timeline\n\
                        4. SRUM\n\
                        5. Prefetch\n\
                        6. Amcache\n\
                        7. IIS Logs\n\
                        Choice: ")
        
        if artifact in inputArtifactChoiceList:
               break
        else:
            print("Please enter a valid option.\n")
    


    # WINDOWS EVENT LOGS LOGIC
    if artifact == "1":
        # Initilize an argument string to be fed into ZimmermanTool

        # Define path of EvtxECmd.exe
        zimmermanExe = zimmermanFolder + 'EvtxECmd.exe'
        
        # Get hostname of asset being analyzed
        hostname = input("Enter hostname you are analyzing: ")

        # Define output csv filename
        csvf = "evtx_" + hostname + ".csv"

        # Determine if a directory or file needs to be parsed.
        inputTypeChoiceList = ["d", "directory", "f", "file"]
        while True:
            inputTypeChoice = input('Parsing a directory or a file?\n\
                                    Enter "d" for directory or "f" for file: ')
            
            if inputTypeChoice.lower() in inputTypeChoiceList:
               break
           
            else:
                print("Please enter a valid option.\n")
            
        # Intialize input arguments for ZimmermanTools
        if inputTypeChoice == "d":
            d = input("Enter directory path: ")
            arguments = arguments + "-d" + " " + '"' + d + '"'
        if inputTypeChoice == "f":
            f = input("Enter file path: ")
            arguments = arguments + "-f" + " " + '"' + f + '"'

        # Determine if a specific timerange is desired.
        inputTimeChoiceList = ["t", "a"]
        while True:
            inputTime = input('Need a specific a timerange? Or do you want the entire input parsed?\n\
               Enter "t" for a specific timerange or "a" for all timeranges: ')
    
            if inputTime.lower() in inputTimeChoiceList:
               break
            
            else:
                print("Please enter a valid option.\n")

        # If timerange is selected, have user define start and end times.
        if inputTime == "t":
            while True:
                inputStartTime = input('Start time (yyyy-MM-dd HH:mm:ss): ') 
                inputEndTime = input('End time (yyyy-MM-dd HH:mm:ss): ')
                
                # Input validation
                timeFormat= "%Y-%m-%d %H:%M:%S"

                if bool(datetime.strptime(timeFormat, timeFormat)) and bool(datetime.strptime(inputEndTime, timeFormat)):
                    # Intialize sd and ed input arguments for ZimmermanTools
                    sd = inputStartTime + ".0000000"
                    ed = inputEndTime + ".0000000"
                    arguments = arguments + " " + "--sd" + " " + sd + " " + "--ed" + " " + ed
                    break
                else:
                    print("Please enter a valid option.\n")

        # Construct final command
        arguments = arguments + " " + "--csv" + + " " + '"' + desktop + '"' + " " + "--csvf" + " " + hostname
        print("[+] Running EvtxECmd.exe with your supplied options.")
        subprocess.run([zimmermanExe, arguments], capture_output = True, text = True)
        print("\n * * * * * * * * * \n")
        print("[+] DONE. Please check the Desktop for the parsed CSV output file.\n")

    # MFT LOGIC

    # MFT TIMELINE LOGIC

    # SRUM LOGIC

    # PREFETCH LOGIC

    # AMCACHE LOGIC

    # IIS Logs








   

