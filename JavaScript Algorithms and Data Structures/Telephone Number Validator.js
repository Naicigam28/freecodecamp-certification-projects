function telephoneCheck(str) {
    // Good luck!
    let test = /^(1\s?)?(\(\d{3}\)|\d{3})[\s\-]?\d{3}[\s\-]?\d{4}$/;
    return test.test(str);
  }
  
  //telephoneCheck("555-555-5555");