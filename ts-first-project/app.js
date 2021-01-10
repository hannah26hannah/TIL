var studentID = 12345;
var studentName = 'Jenny Kim';
var age = 21;
var gender = 'female';
var subject = 'JavaScript';
var courseCompleted = false;
var GenderType;
(function (GenderType) {
    GenderType["Male"] = "male";
    GenderType["Female"] = "female";
    GenderType["GenderNeutral"] = "genderNeutral";
})(GenderType || (GenderType = {}));
var student1 = {
    studentID: 11111,
    studentName: 'Janet Jackson',
    age: 30,
    gender: 'female',
    subject: 'Mongo DB',
    courseCompleted: false
};
function getStudentDetails(studentID) {
    return {
        studentID: 1234567,
        studentName: 'Mark Jacobs',
        // age: 20,
        gender: 'male',
        subject: 'Node JS',
        courseCompleted: true
    };
}
function saveStudentDetail(student) {
    // student.studentID = 12343435;
}
// saveStudentDetail(student1);
