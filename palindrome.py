# Goran Peic, Ph.D.
# Palindrome Exercise

import pandas as pd
import os
import progressbar as pb

def checkPalindrome(number):
  if str(number) == str(number)[::-1]: return True
  else: return False

def main():
  print("Welcome to GP's Lean Mean Palindrome Machine!")
  print("This script searches for and outputs all palindromes (base-10 and base-2) \nwithin a user-specified range.")
  while True:
    try:
      minNum = int(input("Please enter the lower integer: "))
      break
    except ValueError:
      print("Please enter a valid integer.")
  while True:
    try:
      maxNum = int(input("Please enter the upper integer: "))
      break
    except ValueError:
      print("Please enter a valid integer.")
  destFolder = input(r"Please enter output destination folder (e.g., C:\Palindrome): ")
  if not os.path.exists(destFolder): os.makedirs(destFolder)
  destFile = destFolder + "\\All Palindromes Between " + str(minNum) + " and " + str(maxNum) + ".csv"
  dframe = pd.DataFrame({"Decimal": range(minNum, maxNum+1)})
  dframe["Binary"] = ""; dframe["PalInDec"] = dframe["PalInBin"] = False
  bar = pb.ProgressBar(max_value=len(dframe.index))
  for num in range(len(dframe.index)):
    dframe.loc[num, "Binary"] = bin(dframe.loc[num, "Decimal"])[2:]
    if checkPalindrome(dframe.loc[num, "Decimal"]): dframe.loc[num, "PalInDec"] = True
    if checkPalindrome(dframe.loc[num, "Binary"]): dframe.loc[num, "PalInBin"] = True
    bar.update(num)
  dframe = dframe.query("PalInDec == True & PalInBin == True")
  print("\nFound " + str(len(dframe)) + " palindromes between " + str(minNum) + " and " + str(maxNum) + ".")
  print(dframe[["Decimal", "Binary"]])
  print("The sum of all found palindromes is: " + str(dframe["Decimal"].sum()) + ".")
  while True:
    try:
      dframe[["Decimal", "Binary"]].to_csv(destFile, index=False, header=True)
      print("Exported " + destFile + ".")
      break
    except PermissionError:
      print('OS Permissions Error: cannot write to the specified folder.')
      break

if __name__ == "__main__":
  main()