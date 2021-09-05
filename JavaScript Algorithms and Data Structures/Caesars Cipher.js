function rot13(str) { // LBH QVQ VG!
    var alpha="abcdefghijklmnopqrstuvwxyz".toUpperCase();
  
    let i=0;
    let out="";
    for(i;i<str.length;i++)
    {
      if(str.charAt(i)===" "){
        out+=" "
      }
      else if(alpha.indexOf(str.charAt(i))<0)
      {
        out+=str.charAt(i);
      }
      else
      {
        let index=alpha.indexOf(str.charAt(i))+13;
        out+=alpha.charAt(index%26);
      }
    }
    console.log(out);
    return out;
  }
  
  // Change the inputs below to test
  rot13("SERR PBQR PNZC");