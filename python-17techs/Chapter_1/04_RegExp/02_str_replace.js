// str.replace(regexp, replacement) 메서드는 str 내 부분 문자열 중 regexp에 일치하는 부분 문자열을 replacement로 교체한다. /g 플래그의 도움으로 모든 부분 문자열을 교체하거나, 일치하는 첫 번째 부분 문자열만 교체할 수 있다. 

// only i flag
console.log("We will, we will".replace(/we/i, "I")); //I will, we will

// with g flag
console.log("We will, we will".replace(/we/ig, "I")); // I will, I will