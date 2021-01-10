const sendGreeting = (message = "Hello", userName = "this is default"):void => console.log (`${message}, ${userName}`);

sendGreeting(); 
sendGreeting("Good Morning"); 
sendGreeting("Good Night", "Hannah"); 