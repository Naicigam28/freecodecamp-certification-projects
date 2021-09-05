function palindrome(str) {

    let val=str.toLowerCase().replace(/[.,\/#!$%\^&\*;:{}=\-_ _`~()]/g,"");
    let i=0;
    for(i;i<val.length;i++)
    {
      if(val.charAt(i)!==val.charAt(val.length-1-i))
      {
        return false;
      }
    }
    return true;
  }
palindrome("eye");