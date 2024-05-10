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
    print(f'[+] Parsing with your supplied options: {command}.')
    
    while True:
        nextline = process.stdout.readline()
        result = process.poll()
        if result is not None: 
            process.terminate()
            break
        else:
            sys.stdout.write(nextline.decode('utf8'))
  
    print(f'[+] DONE parsing with your supplied options: {command}.\n')
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

def zimmermanMFTBodyFile(command):
    process = subprocess.Popen(command1, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    print(f'[+] Creating a body with your supplied options: {command1}.')
    
    while True:
        nextline = process.stdout.readline()
        result = process.poll()
        if result is not None: 
            process.terminate()
            break
        else:
            sys.stdout.write(nextline.decode('utf8'))
  
    print(f'[+] DONE creating a body file with your supplied options: {command1}.\n')
    print("Please check the current directory for the body file.\n")
        
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
    artifact = ''
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
        workingDirEvtxECmd = os.path.join(os.getcwd(), 'ZimmermanTools\\', 'EvtxECmd\\')
        EvtxECmdPath = os.path.join(workingDirEvtxECmd, 'EvtxECmd.exe')
        
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
            arguments = arguments + f' -d "{dir}"'
        if inputTypeChoice.lower() == "f":
            f = input("Enter file path: ")
            arguments = arguments + f' -f "{f}"'

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
                        arguments = arguments + f' --sd {sd} --ed {ed}'
                        break
                except ValueError:
                    print("Please enter a valid option.\n")
                else:
                    print("Please enter a valid option.\n")
                    
        # Construct final command
        arguments = arguments + f' --csv {desktop} --csvf {csvf}'
        command = EvtxECmdPath + arguments

        # Execute Zimmerman Tool
        zimmermanExecute(command)

############################################

    # MFT LOGIC
    if artifact == "2":
        # Initilize an argument string to be fed into ZimmermanTool
        arguments = " "

        # Define path of MFTECmd.exe
        workingDirMFTECmd = os.path.join(os.getcwd(), 'ZimmermanTools\\')
        MFTECmdPath = os.path.join(workingDirMFTECmd, 'MFTECmd.exe')
        
        # Get hostname of asset being analyzed
        hostname = input("Enter hostname you are analyzing: ")

        # Define output csv filename
        csvf = "MFT_parsed_" + hostname + ".csv"

        # Intialize input arguments for ZimmermanTools
        inputMFTPath = input("What is the path of the file you want parsed?: ")

        # Construct final command
        arguments = arguments + f' -f "{inputMFTPath}" --csv {desktop} --csvf {csvf}'
        command = MFTECmdPath + arguments

        # Execute Zimmerman Tool
        zimmermanExecute(command)

############################################


    # MFT TIMELINE LOGIC
    if artifact == "3":

        # Define path of EvtxECmd.exe
        workingDirMFTECmd2 = os.path.join(os.getcwd(), 'ZimmermanTools\\')
        MFTECmdPath2 = os.path.join(workingDirMFTECmd2, 'MFTECmd.exe')
        
        # Get hostname of asset being analyzed
        hostname = input("Enter hostname you are analyzing: ")

        # Define output csv filename
        csv = "MFT_timeline_" + hostname + ".csv"
       
        # Determine specific timerange that is desired.
        print('Please specify a timerange.\n')
        while True:
            inputStartTime = input('Start time (yyyy-MM-dd): ')
            inputEndTime = input('End time (yyyy-MM-dd): ')

            # Input validation
            timeFormat = '%Y-%m-%d'

            try:
                if bool(datetime.strptime(inputStartTime, timeFormat)) and bool(datetime.strptime(inputEndTime, timeFormat)):
                    # Intialize sd and ed input arguments for ZimmermanTools
                    sd = inputStartTime
                    ed = inputEndTime
                    break
            except ValueError:
                print("Please enter a valid option.\n")
            else:
                print("Please enter a valid option.\n")
        
        # Determine what drive will be parsed
        inputDriveChoice = input("What drive do you want parsed?: ")

        # Intialize input arguments for ZimmermanTools
        inputMFTPath = input("What is the path of the file you want parsed?: ")
                    
        # Construct arguments for first command
        arguments1 = f' -f "{inputMFTPath}" --body .\ --bodyf mft_body --bdl {inputDriveChoice}'
        command1 = MFTECmdPath2 + arguments1

        # Execute Zimmerman Tool to parse a body file.
        zimmermanMFTBodyFile(command1)

        # Open a bash shell and parse a MFT timeline
        command2 = f'bash; sleep 10; mactime -z UTC -d -b mft_body {sd}..{ed} > {inputDriveChoice}_mft_timline.csv'
        process_MFTTimeline = subprocess.Popen(command2, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    
        print(f'[+] Parsing with your MFT Timeline with your supplied options: {command2}.')
    
        while True:
            nextline = process_MFTTimeline.stdout.readline()
            result = process_MFTTimeline.poll()
            if result is not None: 
                process_MFTTimeline.terminate()
                break
            else:
                sys.stdout.write(nextline.decode('utf8'))
  
        print(f'[+] DONE parsing with your MFT Timeline with your supplied options: {command2}.\n')
        print("Please check the Desktop for the parsed CSV output file.\n")


############################################


    # SRUM LOGIC
    if artifact == "4":
        # Initilize an argument string to be fed into ZimmermanTool
        arguments = " "

        # Define path of SrumECmd.exe
        workingDirSrumECmd = os.path.join(os.getcwd(), 'ZimmermanTools\\')
        SrumECmdPath = os.path.join(workingDirSrumECmd, 'SrumECmd.exe')
        
        # Get hostname of asset being analyzed
        hostname = input("Enter hostname you are analyzing: ")

        #Initialize folder to save files to
        saveDir = f'{desktop}\\Srum_Parsed\\'

        # Intialize input arguments for ZimmermanTools
        inputSrumPath = input("What is the path of the file you want parsed?: ")

        # Construct final command
        arguments = arguments + f' -d "{inputSrumPath}" --csv "{saveDir}"'
        command = SrumECmdPath + arguments

        # Execute Zimmerman Tool
        zimmermanExecute(command)


    # PREFETCH LOGIC
    if artifact == "5":
        
        # Initilize an argument string to be fed into ZimmermanTool
        arguments = " "

        # Define path of PECmd.exe
        workingDirPECmd = os.path.join(os.getcwd(), 'ZimmermanTools\\')
        PECmdPath = os.path.join(workingDirPECmd, 'PECmd.exe')
        
        # Get hostname of asset being analyzed
        hostname = input("Enter hostname you are analyzing: ")

        # Define output csv filename
        csvf = "prefetch_parsed_" + hostname + ".csv"
       
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
            arguments = arguments + f' -d "{dir}"'
        if inputTypeChoice.lower() == "f":
            f = input("Enter file path: ")
            arguments = arguments + f' -f "{f}"'
                    
        # Construct final command
        arguments = arguments + f' --csv {desktop} --csvf {csvf}'
        command = PECmdPath + arguments

        # Execute Zimmerman Tool
        zimmermanExecute(command)

    # AMCACHE LOGIC
    if artifact == "6":
        
        # Initilize an argument string to be fed into ZimmermanTool
        arguments = " "

        # Define path of AmcacheParser.exe
        workingDirAmcacheParser = os.path.join(os.getcwd(), 'ZimmermanTools\\')
        AmcacheParserPath = os.path.join(workingDirAmcacheParser, 'AmcacheParser.exe')
        
        # Get hostname of asset being analyzed
        hostname = input("Enter hostname you are analyzing: ")

        # Define output csv filename
        csvf = "amcache_parsed_" + hostname + ".csv"
       
        # Intialize input arguments for ZimmermanTools
        inputFilePath = input("Please enter path of Amcache.hve you want parsed: ")
        arguments = arguments + f'-f "{inputFilePath}"'
                    
        # Construct final command
        arguments = arguments + f' --csv {desktop} --csvf {csvf} --nl'
        command = AmcacheParserPath + arguments

        # Execute Zimmerman Tool
        zimmermanExecute(command)

    # IIS Logs
