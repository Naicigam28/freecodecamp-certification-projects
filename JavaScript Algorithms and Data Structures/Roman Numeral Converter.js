function convertToRoman(num) {
    var decimalValue = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1];
  var romanNumeral = [
    "M",
    "CM",
    "D",
    "CD",
    "C",
    "XC",
    "L",
    "XL",
    "X",
    "IX",
    "V",
    "IV",
    "I"
  ];
  let str="";
  let i=0;
for(i;i<decimalValue.length;i++)
{while(num>=decimalValue[i])
    {
        num-=decimalValue[i];
        console.log(num,decimalValue[i]);
        str+=romanNumeral[i];
    }
}
console.log(str)
 return str;
}

convertToRoman(36);