var sendGreeting = function (message, userName) {
    if (message === void 0) { message = "Hello"; }
    if (userName === void 0) { userName = "this is default"; }
    return console.log(message + ", " + userName);
};
sendGreeting();
sendGreeting("Good Morning");
sendGreeting("Good Night", "Hannah");
