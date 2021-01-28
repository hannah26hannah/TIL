// str.match로 검색하기

// 1. /g 
let str = "We will, we will rock you";
console.log(str.match(/we/gi)); // ["We", "we"]

// 2. without g flag
let result = str.match(/we/i);

console.log(result[0]); // We
console.log(result[1]); // undefined global flag가 없으므로 we와 매치되는 최초의 검색 결과만 반환되기 때문.
console.log(result.length); // 1
console.log(result.index); // 0 부분 문자열의 위치
console.log(result.input); // We will, we will rock you

// 3. when data not found
// g flag의 유무와 무관하게, 일치하는 부분 문자열이 없다면, 빈 배열을 반환하는 것이 아니라 null을 반환한다. 
let matches = "JavaScript".match(/HTML/); // matches에 null이 저장됨
if (!matches.length) { // Uncaught TypeError: matches is null therefore can't read property 'length' of null
    console.log("에러")
}

// 4. returns always array even when data is not found
let matches = "JavaScript".match(/HTML/) || [];
if (!matches.length) {
    console.log("정규 표현식과 일치하는 부분 문자열이 없습니다.")
}