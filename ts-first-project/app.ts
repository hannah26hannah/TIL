let studentID:number = 12345;
let studentName:string = 'Jenny Kim';
let age:number = 21;
let gender:string = 'female';
let subject:string = 'JavaScript';
let courseCompleted:boolean = false;

enum GenderType {
    Male = 'male',
    Female = 'female',
    GenderNeutral = 'genderNeutral'
}

let student1 = {
    studentID: 11111,
    studentName: 'Janet Jackson',
    age: 30,
    gender: 'female',
    subject: 'Mongo DB',
    courseCompleted: false
}

interface Student {
    readonly studentID: number;
    studentName: string;
    age?: number;
    gender: 'male' | 'female' | 'genderNeutral';
    subject: string;
    courseCompleted: boolean;
    // addComment (comment: string): string;
    addComment?: (comment:string) => string;
}

function getStudentDetails(studentID: number): Student {
    return {
        studentID: 1234567,
        studentName: 'Mark Jacobs',
        // age: 20,
        gender: 'male',
        subject: 'Node JS',
        courseCompleted: true
    }
}

function saveStudentDetail (student: Student):void {
    // student.studentID = 12343435;
}

 

// saveStudentDetail(student1);