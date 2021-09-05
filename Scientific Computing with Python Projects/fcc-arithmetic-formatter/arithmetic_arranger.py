import re

def arithmetic_arranger(problems,wantsAnswer=False):
  
  if(len(problems)>5):
    return "Error: Too many problems."
  arranged_problems=""
  line1=""
  line2=""
  line3=""
  line4=""
  operators='\s[\+/*-]\s'
  for problem in problems:
    
    op=re.search(operators,problem)[0].strip()
    if(op!="+" and op!="-"):
      arranged_problems="Error: Operator must be '+' or '-'."
      break
      
    length=getLongestLenght
    lines=problem.split(op)
    val1=lines[0].strip()
    val2=lines[1].strip()
    answer=None
    try:
      answer=calcAnswer(val1,val2,op)
    except:
      arranged_problems="Error: Numbers must only contain digits."
      break
    length=getLongestLenght(val1,val2)
    if(length>4):
      arranged_problems="Error: Numbers cannot be more than four digits."
      break
    length=length+2
    if(problem == problems[-1]):
      line1=line1+formatNumbers(val1,length)
      line2=line2+formatNumbers(val2,length,op)
      line4=line4+formatNumbers(answer,length)
      
      for i in range(0,length):
        line3=line3+"-"
      line3=line3
    else:
      line1=line1+formatNumbers(val1,length)+'    '
      line2=line2+formatNumbers(val2,length,op)+'    '
      line4=line4+formatNumbers(answer,length)+'    '
      for i in range(0,length):
        line3=line3+"-"
      line3=line3+"    "
  
  if(wantsAnswer and arranged_problems==""):
    arranged_problems=f"{line1}\n{line2}\n{line3}\n{line4}"
  if(arranged_problems==""):
    arranged_problems=f"{line1}\n{line2}\n{line3}"
  
  return arranged_problems

def formatNumbers(number,length,operator=" "):
  out=""
  
  for i in range(1,length-len(str(number))):
  
    out=" "+out

  return f"{operator}{out}{number}"

def getLongestLenght(str1,str2):
  if(len(str1)>len(str2)):
    return len(str1)
  return len(str2)

def calcAnswer(val1,val2,operator):
  if(operator=="+"):
    return int(val1)+int(val2)
  return int(val1)-int(val2)
